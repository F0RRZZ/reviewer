import django.db.models

import core.base_models
import core.mixins
import movies.managers


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

    def get_image_path(self, filename: str) -> str:
        return f'movies/movie_{self.id}/{filename}'

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
        auto_now=True,
    )

    objects = movies.managers.MovieManager()

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
