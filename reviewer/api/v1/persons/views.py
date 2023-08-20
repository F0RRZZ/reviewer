from rest_framework.viewsets import ModelViewSet

from api.v1.persons.serializers import PersonSerializer
from core.api.permissions import IsAdminOrReadOnly
from persons.models import Person


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAdminOrReadOnly,)
