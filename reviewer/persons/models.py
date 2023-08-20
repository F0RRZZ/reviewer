from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import safestring, timezone

from core.mixins import ImageMixin
from genres.models import Genre
from roles.models import Role


class Person(ImageMixin, models.Model):
    DEFAULT_IMAGE = 'images/default_avatar.png'
    name = models.CharField(
        'name',
        max_length=50,
        help_text='Maximum of 50 symbols',
    )
    surname = models.CharField(
        'surname', max_length=50, help_text='Maximum of 50 symbols'
    )
    career = models.ManyToManyField(
        Role,
    )
    height = models.PositiveSmallIntegerField(
        'height',
        validators=[
            MinValueValidator(100),
            MaxValueValidator(250),
        ],
        help_text='Min - 120, max - 250',
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        'date_of_birth',
        null=True,
        blank=True,
    )
    place_of_birth = models.CharField(
        'place_of_birth',
        max_length=200,
        help_text='Maximum of 200 symbols',
        null=True,
        blank=True,
    )
    genres = models.ManyToManyField(
        Genre,
    )

    def get_image_path(self, filename: str) -> str:
        return f'persons/person_{self.id}/{filename}'

    image = models.ImageField(
        'image',
        upload_to=get_image_path,
        default=DEFAULT_IMAGE,
    )

    def image_tmb(self):
        if self.image:
            image_url = self.image.url
            return safestring.mark_safe(
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
            self.date_of_birth = timezone.now()
        super(Person, self).save(*args, **kwargs)
