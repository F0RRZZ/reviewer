import django.db.models
import django.utils.safestring

import core.base_models
import core.mixins
import genres.models
import movies.managers
import persons.models


class Movie(core.base_models.NameFormatterBaseModel, core.mixins.ImageMixin):
    DEFAULT_IMAGE = 'images/default_movie_image.jpeg'

    name = django.db.models.CharField(
        'name', max_length=100, help_text='Maximum of 100 symbols'
    )
    formatted_name = django.db.models.CharField(
        'formatted_name',
        max_length=100,
        editable=False,
    )
    description = django.db.models.TextField(
        'description', max_length=1000, help_text='Maximum of 1000 symbols'
    )
    genre = django.db.models.ManyToManyField(
        genres.models.Genre,
    )
    country = django.db.models.CharField(
        'country',
        max_length=50,
        help_text='Maximum of 50 symbols',
        null=True,
        blank=True,
    )
    actors = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='actors',
        blank=True,
    )
    director = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='director',
        blank=True,
    )
    producer = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='producer',
        blank=True,
    )
    screenwriter = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='screenwriter',
        blank=True,
    )
    operator = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='operator',
        blank=True,
    )
    composer = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='composer',
        blank=True,
    )
    artist = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='artist',
        blank=True,
    )
    montage = django.db.models.ManyToManyField(
        persons.models.Person,
        related_name='montage',
        blank=True,
    )
    budget = django.db.models.PositiveIntegerField(
        'budget',
        null=True,
        blank=True,
    )

    def get_image_path(self, filename: str) -> str:
        return f'movies/movie_{self.id}/{filename}'

    kinopoisk_link = django.db.models.CharField(
        'kinopoisk_link',
        max_length=500,
        null=True,
        blank=True,
    )
    imdb_link = django.db.models.CharField(
        'imdb_link',
        max_length=500,
        null=True,
        blank=True,
    )
    image = django.db.models.ImageField(
        'image',
        upload_to=get_image_path,
        null=True,
        default=DEFAULT_IMAGE,
    )
    created_at = django.db.models.DateField(
        'created_at',
        editable=True,
    )
    uploaded_at = django.db.models.DateField(
        'uploaded_at',
        editable=False,
        auto_now_add=True,
    )

    objects = movies.managers.MovieManager()

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.name[:50]

    def image_tmb(self):
        if self.image:
            image_url = self.image.url
            return django.utils.safestring.mark_safe(
                f'<img src="{image_url}" width="50" height="50"/>'
            )
        return 'no_photo'

    image_tmb.short_description = 'image'
    image_tmb.allow_tags = True
