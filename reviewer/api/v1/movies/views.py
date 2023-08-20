from rest_framework.viewsets import ModelViewSet

from api.v1.movies.serializers import MovieSerializer
from core.api.permissions import IsAdminOrReadOnly
from movies.models import Movie


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)
