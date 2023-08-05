import rest_framework.viewsets

import api.v1.roles.serializers
import core.api.permissions
import roles.models


class RoleViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = roles.models.Role.objects.all()
    serializer_class = api.v1.roles.serializers.RoleSerializer
    permission_classes = (core.api.permissions.IsAdminOrReadOnly,)
