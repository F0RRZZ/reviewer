from django.contrib.admin import ModelAdmin, register

from rating.models import Rating


@register(Rating)
class RatingAdmin(ModelAdmin):
    list_display = (
        Rating.movie.field.name,
        Rating.total_rating.field.name,
    )
    readonly_fields = (
        Rating.total_rating.field.name,
        Rating.created_at.field.name,
    )
