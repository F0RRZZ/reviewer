from rest_framework.serializers import ModelSerializer

from api.v1.genres.serializers import GenreSerializer
from api.v1.roles.serializers import RoleSerializer
from persons.models import Person


class PersonSerializer(ModelSerializer):
    genres = GenreSerializer(
        many=True,
        read_only=True,
    )
    career = RoleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Person
        fields = (
            Person.name.field.name,
            Person.surname.field.name,
            Person.career.field.name,
            Person.height.field.name,
            Person.date_of_birth.field.name,
            Person.place_of_birth.field.name,
            Person.genres.field.name,
        )
