import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.urls
import homepage.views

urlpatterns = [
    django.urls.path('', homepage.views.HomepageView.as_view()),
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
