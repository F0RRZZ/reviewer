from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
from django.urls import include, path

urlpatterns = [
    path('', include('feeds.urls', namespace='feeds')),
    path('genres/', include('genres.urls', namespace='genres')),
    path('movies/', include('movies.urls', namespace='movies')),
    path('person/', include('persons.urls', namespace='persons')),
    path('user/', include('users.urls', namespace='users')),
    path(
        'user/',
        include('django.contrib.auth.urls'),
    ),
    path(
        'api/v1/',
        include('api.urls'),
    ),
    path('admin/', site.urls),
] + (
    static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(
            '__debug__/',
            include(debug_toolbar.urls),
        )
    ]
