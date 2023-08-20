from rest_framework.viewsets import ModelViewSet

from api.v1.users.serializers import UserSerializer
from core.api.permissions import IsAdminOrReadOnly
from users.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)
