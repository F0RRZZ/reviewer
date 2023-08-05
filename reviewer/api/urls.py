import django.urls

import api.v1.genres.routers
import api.v1.movies.routers
import api.v1.persons.routers
import api.v1.roles.routers
import api.v1.users.routers

app_name = 'api'
urlpatterns = [
    django.urls.path(
        '',
        django.urls.include(api.v1.users.routers.router.urls),
    ),
    django.urls.path(
        '',
        django.urls.include(api.v1.movies.routers.router.urls),
    ),
    django.urls.path(
        '',
        django.urls.include(api.v1.persons.routers.router.urls),
    ),
    django.urls.path(
        '',
        django.urls.include(api.v1.roles.routers.router.urls),
    ),
    django.urls.path(
        '',
        django.urls.include(api.v1.genres.routers.router.urls),
    ),
]
