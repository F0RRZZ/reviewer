from django.urls import include, path

from api.v1.genres.routers import router as genres_router
from api.v1.movies.routers import router as movies_router
from api.v1.persons.routers import router as persons_router
from api.v1.roles.routers import router as roles_router
from api.v1.users.routers import router as users_router

app_name = 'api'
urlpatterns = [
    path(
        '',
        include(users_router.urls),
    ),
    path(
        '',
        include(movies_router.urls),
    ),
    path(
        '',
        include(persons_router.urls),
    ),
    path(
        '',
        include(roles_router.urls),
    ),
    path(
        '',
        include(genres_router.urls),
    ),
]
