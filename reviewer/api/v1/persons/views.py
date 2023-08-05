import rest_framework.viewsets

import api.v1.persons.serializers
import core.api.permissions
import persons.models


class PersonViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = persons.models.Person.objects.all()
    serializer_class = api.v1.persons.serializers.PersonSerializer
    permission_classes = (core.api.permissions.IsAdminOrReadOnly,)
