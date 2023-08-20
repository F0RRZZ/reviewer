from django.contrib.admin import ModelAdmin, register

from genres.models import Genre


@register(Genre)
class GenreAdmin(ModelAdmin):
    exclude = (Genre.formatted_name.field.name,)
