import rest_framework.routers

import api.v1.genres.views

router = rest_framework.routers.DefaultRouter()
router.register(
    r'genres',
    api.v1.genres.views.GenreViewSet,
    basename='genres',
)
