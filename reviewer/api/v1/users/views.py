import rest_framework.viewsets

import api.v1.users.serializers
import core.api.permissions
import users.models


class UserViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = users.models.User.objects.all()
    serializer_class = api.v1.users.serializers.UserSerializer
    permission_classes = (core.api.permissions.IsAdminOrReadOnly,)
