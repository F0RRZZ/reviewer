from rest_framework.routers import DefaultRouter

from api.v1.genres.views import GenreViewSet

router = DefaultRouter()
router.register(
    r'genres',
    GenreViewSet,
    basename='genres',
)
