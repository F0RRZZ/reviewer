import rest_framework.viewsets

import api.v1.genres.serializers
import core.api.permissions
import genres.models


class GenreViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = genres.models.Genre.objects.all()
    serializer_class = api.v1.genres.serializers.GenreSerializer
    permission_classes = (core.api.permissions.IsAdminOrReadOnly,)
