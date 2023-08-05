import rest_framework.routers

import api.v1.persons.views

router = rest_framework.routers.DefaultRouter()
router.register(
    r'persons',
    api.v1.persons.views.PersonViewSet,
    basename='persons',
)
