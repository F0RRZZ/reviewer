import django.contrib.admin

import roles.models


@django.contrib.admin.register(roles.models.Role)
class GenreAdmin(django.contrib.admin.ModelAdmin):
    exclude = (roles.models.Role.formatted_name.field.name,)
