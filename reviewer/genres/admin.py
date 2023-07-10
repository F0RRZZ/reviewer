import django.contrib.admin

import genres.models


@django.contrib.admin.register(genres.models.Genre)
class GenreAdmin(django.contrib.admin.ModelAdmin):
    exclude = (genres.models.Genre.formatted_name.field.name,)
