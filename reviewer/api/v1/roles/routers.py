from rest_framework.routers import DefaultRouter

from api.v1.roles.views import RoleViewSet

router = DefaultRouter()
router.register(
    r'roles',
    RoleViewSet,
    basename='roles',
)
