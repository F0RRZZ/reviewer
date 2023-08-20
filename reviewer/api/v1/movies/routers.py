from rest_framework.routers import DefaultRouter

from api.v1.movies.views import MovieViewSet

router = DefaultRouter()
router.register(
    r'movies',
    MovieViewSet,
    basename='movies',
)
