from django.db import models
from django.utils.safestring import mark_safe

from core.base_models import NameFormatterBaseModel
from core.mixins import ImageMixin
from genres.models import Genre
from movies.managers import MovieManager
from persons.models import Person


class Movie(NameFormatterBaseModel, ImageMixin):
    DEFAULT_IMAGE = 'images/default_movie_image.jpeg'

    name = models.CharField(
        'name', max_length=100, help_text='Maximum of 100 symbols'
    )
    formatted_name = models.CharField(
        'formatted_name',
        max_length=100,
        editable=False,
    )
    description = models.TextField(
        'description', max_length=1000, help_text='Maximum of 1000 symbols'
    )
    genre = models.ManyToManyField(
        Genre,
    )
    country = models.CharField(
        'country',
        max_length=50,
        help_text='Maximum of 50 symbols',
        null=True,
        blank=True,
    )
    actors = models.ManyToManyField(
        Person,
        related_name='actors',
        blank=True,
    )
    director = models.ManyToManyField(
        Person,
        related_name='director',
        blank=True,
    )
    producer = models.ManyToManyField(
        Person,
        related_name='producer',
        blank=True,
    )
    screenwriter = models.ManyToManyField(
        Person,
        related_name='screenwriter',
        blank=True,
    )
    operator = models.ManyToManyField(
        Person,
        related_name='operator',
        blank=True,
    )
    composer = models.ManyToManyField(
        Person,
        related_name='composer',
        blank=True,
    )
    artist = models.ManyToManyField(
        Person,
        related_name='artist',
        blank=True,
    )
    montage = models.ManyToManyField(
        Person,
        related_name='montage',
        blank=True,
    )
    budget = models.PositiveIntegerField(
        'budget',
        null=True,
        blank=True,
    )

    def get_image_path(self, filename: str) -> str:
        return f'movies/movie_{self.id}/{filename}'

    kinopoisk_link = models.CharField(
        'kinopoisk_link',
        max_length=500,
        null=True,
        blank=True,
    )
    imdb_link = models.CharField(
        'imdb_link',
        max_length=500,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        'image',
        upload_to=get_image_path,
        null=True,
        default=DEFAULT_IMAGE,
    )
    created_at = models.DateField(
        'created_at',
        editable=True,
    )
    uploaded_at = models.DateField(
        'uploaded_at',
        editable=False,
        auto_now_add=True,
    )

    objects = MovieManager()

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.name[:50]

    def image_tmb(self):
        if self.image:
            image_url = self.image.url
            return mark_safe(
                f'<img src="{image_url}" width="50" height="50"/>'
            )
        return 'no_photo'

    image_tmb.short_description = 'image'
    image_tmb.allow_tags = True
