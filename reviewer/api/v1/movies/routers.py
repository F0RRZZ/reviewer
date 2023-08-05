import rest_framework.routers

import api.v1.movies.views

router = rest_framework.routers.DefaultRouter()
router.register(
    r'movies',
    api.v1.movies.views.MovieViewSet,
    basename='movies',
)
