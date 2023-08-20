from django.contrib.admin import ModelAdmin, register

from movies.models import Movie


@register(Movie)
class MoviesAdmin(ModelAdmin):
    fields = (
        Movie.name.field.name,
        Movie.description.field.name,
        Movie.image.field.name,
        Movie.genre.field.name,
        Movie.created_at.field.name,
        Movie.country.field.name,
        Movie.director.field.name,
        Movie.producer.field.name,
        Movie.screenwriter.field.name,
        Movie.operator.field.name,
        Movie.composer.field.name,
        Movie.artist.field.name,
        Movie.montage.field.name,
        Movie.actors.field.name,
        Movie.budget.field.name,
        Movie.kinopoisk_link.field.name,
        Movie.imdb_link.field.name,
    )
    filter_horizontal = (
        Movie.genre.field.name,
        Movie.director.field.name,
        Movie.producer.field.name,
        Movie.screenwriter.field.name,
        Movie.operator.field.name,
        Movie.composer.field.name,
        Movie.artist.field.name,
        Movie.montage.field.name,
        Movie.actors.field.name,
    )
    list_display = (
        Movie.name.field.name,
        Movie.created_at.field.name,
        Movie.image_tmb,
    )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == Movie.director.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='режиссер'
            )
        elif db_field.name == Movie.actors.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='актер'
            )
        elif db_field.name == Movie.producer.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='продюсер'
            )
        elif db_field.name == Movie.screenwriter.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='сценарист'
            )
        elif db_field.name == Movie.operator.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='оператор'
            )
        elif db_field.name == Movie.composer.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='композитор'
            )
        elif db_field.name == Movie.artist.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='художник'
            )
        elif db_field.name == Movie.montage.field.name:
            kwargs['queryset'] = db_field.related_model.objects.filter(
                career__name='монтажер'
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)
