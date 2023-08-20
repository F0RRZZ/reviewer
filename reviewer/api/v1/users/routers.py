from rest_framework.routers import DefaultRouter

from api.v1.users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
