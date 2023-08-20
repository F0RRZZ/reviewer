from rest_framework.viewsets import ModelViewSet

from api.v1.roles.serializers import RoleSerializer
from core.api.permissions import IsAdminOrReadOnly
from roles.models import Role


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAdminOrReadOnly,)
