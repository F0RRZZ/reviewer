import rest_framework.viewsets

import api.v1.movies.serializers
import core.api.permissions
import movies.models


class MovieViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = movies.models.Movie.objects.all()
    serializer_class = api.v1.movies.serializers.MovieSerializer
    permission_classes = (core.api.permissions.IsAdminOrReadOnly,)
