from django.contrib.admin import ModelAdmin, register

from persons.models import Person


@register(Person)
class PersonAdmin(ModelAdmin):
    list_display = (
        Person.name.field.name,
        Person.surname.field.name,
        Person.image_tmb,
    )
    fields = (
        Person.name.field.name,
        Person.surname.field.name,
        Person.height.field.name,
        Person.place_of_birth.field.name,
        Person.date_of_birth.field.name,
        Person.image.field.name,
        Person.career.field.name,
        Person.genres.field.name,
    )
    filter_horizontal = (
        Person.career.field.name,
        Person.genres.field.name,
    )
