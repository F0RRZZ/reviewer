from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.mixins import ImageMixin
from users.managers import UserManager


class NormalizedEmailField(models.EmailField):
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


class User(AbstractBaseUser, PermissionsMixin, ImageMixin):
    DEFAULT_IMAGE = 'images/default_avatar.png'

    username = models.CharField(
        'username',
        max_length=50,
        help_text='Maximum of 50 symbols',
        unique=True,
    )
    bio = models.TextField(
        'bio',
        max_length=500,
        help_text='Maximum of 500 symbols',
        default='',
        null=True,
        blank=True,
    )
    email = models.EmailField(
        'email',
        unique=True,
    )
    normalized_email = NormalizedEmailField(
        'normalized_email',
        unique=True,
    )

    def get_image_path(self, filename: str) -> str:
        return f'avatars/user_{self.id}/{filename}'

    image = models.ImageField(
        'avatar',
        upload_to=get_image_path,
        default=DEFAULT_IMAGE,
    )
    date_joined = models.DateTimeField(
        'date_joined',
        auto_now=True,
    )
    is_active = models.BooleanField(
        'active',
        default=False,
    )
    is_staff = models.BooleanField(
        'staff',
        default=False,
    )
    is_superuser = models.BooleanField(
        'superuser',
        default=False,
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def natural_key(self):
        return self.username

    def save(self, *args, **kwargs):
        self.normalized_email = self.normalized_email or self.email
        super(User, self).save(*args, **kwargs)
