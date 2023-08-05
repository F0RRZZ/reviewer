import rest_framework.serializers

import api.v1.genres.serializers
import api.v1.roles.serializers
import persons.models


class PersonSerializer(rest_framework.serializers.ModelSerializer):
    genres = api.v1.genres.serializers.GenreSerializer(
        many=True,
        read_only=True,
    )
    career = api.v1.roles.serializers.RoleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = persons.models.Person
        fields = (
            persons.models.Person.name.field.name,
            persons.models.Person.surname.field.name,
            persons.models.Person.career.field.name,
            persons.models.Person.height.field.name,
            persons.models.Person.date_of_birth.field.name,
            persons.models.Person.place_of_birth.field.name,
            persons.models.Person.genres.field.name,
        )
