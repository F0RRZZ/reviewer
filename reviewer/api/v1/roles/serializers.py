import rest_framework.serializers

import roles.models


class RoleSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = roles.models.Role
        fields = (
            'id',
            roles.models.Role.name.field.name,
        )
