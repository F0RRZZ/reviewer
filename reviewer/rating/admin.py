import django.contrib.admin

import rating.models


@django.contrib.admin.register(rating.models.Rating)
class RatingAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        rating.models.Rating.movie.field.name,
        rating.models.Rating.total_rating.field.name,
    )
    readonly_fields = (rating.models.Rating.total_rating.field.name,)
