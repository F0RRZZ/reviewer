from rest_framework.serializers import ModelSerializer

from roles.models import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id',
            Role.name.field.name,
        )
