from django.contrib.admin import ModelAdmin, register

from roles.models import Role


@register(Role)
class GenreAdmin(ModelAdmin):
    exclude = (Role.formatted_name.field.name,)
