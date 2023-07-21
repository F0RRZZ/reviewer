import django.urls
import django.views.decorators.cache

import feeds.views

app_name = 'feeds'
urlpatterns = [
    django.urls.path(
        '',
        django.views.decorators.cache.cache_page(43200)(
            feeds.views.NewMoviesView.as_view()
        ),
    ),
    django.urls.path(
        'new/',
        django.views.decorators.cache.cache_page(43200)(
            feeds.views.NewMoviesView.as_view()
        ),
    ),
    django.urls.path(
        'recently_added/',
        django.views.decorators.cache.cache_page(43200)(
            feeds.views.RecentlyAddedMoviesView.as_view()
        ),
    ),
    django.urls.path(
        'best/',
        feeds.views.BestMoviesView.as_view(),
    ),
]
