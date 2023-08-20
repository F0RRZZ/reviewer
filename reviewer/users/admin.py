from django.contrib.admin import ModelAdmin, register

from users.models import User


@register(User)
class UserAdmin(ModelAdmin):
    exclude = (
        User.password.field.name,
        User.normalized_email.field.name,
    )
