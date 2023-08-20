from rest_framework.viewsets import ModelViewSet

from api.v1.genres.serializers import GenreSerializer
from core.api.permissions import IsAdminOrReadOnly
from genres.models import Genre


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
