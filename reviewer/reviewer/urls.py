import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.urls

urlpatterns = [
    django.urls.path('', django.urls.include('feeds.urls', namespace='feeds')),
    django.urls.path(
        'genres/', django.urls.include('genres.urls', namespace='genres')
    ),
    django.urls.path(
        'movies/', django.urls.include('movies.urls', namespace='movies')
    ),
    django.urls.path(
        'person/', django.urls.include('persons.urls', namespace='persons')
    ),
    django.urls.path(
        'user/', django.urls.include('users.urls', namespace='users')
    ),
    django.urls.path(
        'user/',
        django.urls.include('django.contrib.auth.urls'),
    ),
    django.urls.path('admin/', django.contrib.admin.site.urls),
] + (
    django.conf.urls.static.static(
        django.conf.settings.MEDIA_URL,
        document_root=django.conf.settings.MEDIA_ROOT,
    )
)

if django.conf.settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        django.urls.path(
            '__debug__/',
            django.urls.include(debug_toolbar.urls),
        )
    ]
