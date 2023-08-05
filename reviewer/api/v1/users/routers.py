import rest_framework.routers

import api.v1.users.views

router = rest_framework.routers.DefaultRouter()
router.register(r'users', api.v1.users.views.UserViewSet, basename='users')
