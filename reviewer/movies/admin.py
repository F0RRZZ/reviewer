import django.contrib.admin

import movies.models


@django.contrib.admin.register(movies.models.Movie)
class MoviesAdmin(django.contrib.admin.ModelAdmin):
    fields = (
        movies.models.Movie.name.field.name,
        movies.models.Movie.description.field.name,
        movies.models.Movie.image.field.name,
        movies.models.Movie.genre.field.name,
        movies.models.Movie.created_at.field.name,
    )
    filter_horizontal = (movies.models.Movie.genre.field.name,)
    list_display = (
        movies.models.Movie.name.field.name,
        movies.models.Movie.created_at.field.name,
        movies.models.Movie.image_tmb,
    )
