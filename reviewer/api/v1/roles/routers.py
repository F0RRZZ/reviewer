import rest_framework.routers

import api.v1.roles.views

router = rest_framework.routers.DefaultRouter()
router.register(
    r'roles',
    api.v1.roles.views.RoleViewSet,
    basename='roles',
)
