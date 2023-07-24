import django.core.validators
import django.db.models
import django.utils.timezone

import core.mixins
import genres.models
import roles.models


class Person(core.mixins.ImageMixin, django.db.models.Model):
    DEFAULT_IMAGE = 'images/default_avatar.png'
    name = django.db.models.CharField(
        'name',
        max_length=50,
        help_text='Maximum of 50 symbols',
    )
    surname = django.db.models.CharField(
        'surname', max_length=50, help_text='Maximum of 50 symbols'
    )
    career = django.db.models.ManyToManyField(
        roles.models.Role,
    )
    height = django.db.models.PositiveSmallIntegerField(
        'height',
        validators=[
            django.core.validators.MinValueValidator(100),
            django.core.validators.MaxValueValidator(250),
        ],
        help_text='Min - 120, max - 250',
        null=True,
        blank=True,
    )
    date_of_birth = django.db.models.DateField(
        'date_of_birth',
        null=True,
        blank=True,
    )
    place_of_birth = django.db.models.CharField(
        'place_of_birth',
        max_length=200,
        help_text='Maximum of 200 symbols',
        null=True,
        blank=True,
    )
    genres = django.db.models.ManyToManyField(
        genres.models.Genre,
    )

    def get_image_path(self, filename: str) -> str:
        return f'persons/person_{self.id}/{filename}'

    image = django.db.models.ImageField(
        'image',
        upload_to=get_image_path,
        default=DEFAULT_IMAGE,
    )

    def image_tmb(self):
        if self.image:
            image_url = self.image.url
            return django.utils.safestring.mark_safe(
                f'<img src="{image_url}" width="50" height="50"/>'
            )
        return 'no_photo'

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    def __str__(self):
        return self.name + ' ' + self.surname

    def save(self, *args, **kwargs):
        if self.date_of_birth is None:
            self.date_of_birth = django.utils.timezone.now()
        super(Person, self).save(*args, **kwargs)
