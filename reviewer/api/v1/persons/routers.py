from rest_framework.routers import DefaultRouter

from api.v1.persons.views import PersonViewSet

router = DefaultRouter()
router.register(
    r'persons',
    PersonViewSet,
    basename='persons',
)
