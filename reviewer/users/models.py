import os

import django.contrib.auth.models
import django.db.models

import core.mixins
import users.managers


class NormalizedEmailField(django.db.models.EmailField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = value.lower()
        if value:
            if '@ya.ru' in value:
                value = value.split('@')[0] + 'yandex.ru'
            if '+' in value:
                value = (
                    f'{value.split("@")[0].split("+")[0]}@'
                    f'{value.split("@")[-1]}'
                )
            username, domain = value.split('@')
            if domain == 'gmail.com':
                username = username.replace('.', '')
            elif domain == 'yandex.ru':
                username = username.replace('.', '-')
            value = f'{username}@{domain}'
        return value


class User(
    django.contrib.auth.models.AbstractBaseUser,
    django.contrib.auth.models.PermissionsMixin,
    core.mixins.ImageMixin,
):
    DEFAULT_IMAGE = 'images/default_avatar.png'

    username = django.db.models.CharField(
        'username',
        max_length=50,
        help_text='Maximum of 50 symbols',
        unique=True,
    )
    bio = django.db.models.TextField(
        'bio',
        max_length=500,
        help_text='Maximum of 500 symbols',
        default='',
    )
    email = django.db.models.EmailField(
        'email',
        unique=True,
    )
    normalized_email = NormalizedEmailField(
        'normalized_email',
        unique=True,
    )

    objects = users.managers.UserManager()

    def get_image_path(self, filename: str):
        extension = filename.split('.')[-1]
        return f'avatars/user_{self.id}.{extension}'

    image = django.db.models.ImageField(
        'avatar',
        upload_to=get_image_path,
        default=DEFAULT_IMAGE,
    )
    date_joined = django.db.models.DateTimeField(
        'date_joined',
        auto_now=True,
    )
    is_active = django.db.models.BooleanField(
        'active',
        default=False,
    )
    is_staff = django.db.models.BooleanField(
        'staff',
        default=False,
    )
    is_superuser = django.db.models.BooleanField(
        'superuser',
        default=False,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def natural_key(self):
        return self.username

    def save(self, *args, **kwargs):
        self.normalized_email = self.normalized_email or self.email
        super(User, self).save(*args, **kwargs)
