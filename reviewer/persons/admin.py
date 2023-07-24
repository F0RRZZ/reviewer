import django.contrib.admin

import persons.models


@django.contrib.admin.register(persons.models.Person)
class PersonAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        persons.models.Person.name.field.name,
        persons.models.Person.surname.field.name,
        persons.models.Person.image_tmb,
    )
    fields = (
        persons.models.Person.name.field.name,
        persons.models.Person.surname.field.name,
        persons.models.Person.height.field.name,
        persons.models.Person.place_of_birth.field.name,
        persons.models.Person.date_of_birth.field.name,
        persons.models.Person.image.field.name,
        persons.models.Person.career.field.name,
        persons.models.Person.genres.field.name,
    )
    filter_horizontal = (
        persons.models.Person.career.field.name,
        persons.models.Person.genres.field.name,
    )
