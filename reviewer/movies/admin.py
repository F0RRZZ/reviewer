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
        movies.models.Movie.country.field.name,
        movies.models.Movie.director.field.name,
        movies.models.Movie.producer.field.name,
        movies.models.Movie.screenwriter.field.name,
        movies.models.Movie.operator.field.name,
        movies.models.Movie.composer.field.name,
        movies.models.Movie.artist.field.name,
        movies.models.Movie.montage.field.name,
        movies.models.Movie.actors.field.name,
        movies.models.Movie.budget.field.name,
        movies.models.Movie.kinopoisk_link.field.name,
        movies.models.Movie.imdb_link.field.name,
    )
    filter_horizontal = (
        movies.models.Movie.genre.field.name,
        movies.models.Movie.director.field.name,
        movies.models.Movie.producer.field.name,
        movies.models.Movie.screenwriter.field.name,
        movies.models.Movie.operator.field.name,
        movies.models.Movie.composer.field.name,
        movies.models.Movie.artist.field.name,
        movies.models.Movie.montage.field.name,
        movies.models.Movie.actors.field.name,
    )
    list_display = (
        movies.models.Movie.name.field.name,
        movies.models.Movie.created_at.field.name,
        movies.models.Movie.image_tmb,
    )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == movies.models.Movie.director.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='режиссер'
            )
        elif db_field.name == movies.models.Movie.actors.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='актер'
            )
        elif db_field.name == movies.models.Movie.producer.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='продюсер'
            )
        elif db_field.name == movies.models.Movie.screenwriter.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='сценарист'
            )
        elif db_field.name == movies.models.Movie.operator.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='оператор'
            )
        elif db_field.name == movies.models.Movie.composer.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='композитор'
            )
        elif db_field.name == movies.models.Movie.artist.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='художник'
            )
        elif db_field.name == movies.models.Movie.montage.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='монтажер'
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)
