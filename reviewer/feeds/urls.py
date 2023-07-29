import django.urls

import feeds.views

app_name = 'feeds'
urlpatterns = [
    django.urls.path(
        '',
        feeds.views.NewMoviesView.as_view(),
        name='new',
    ),
    django.urls.path(
        'new/',
        feeds.views.NewMoviesView.as_view(),
        name='new',
    ),
    django.urls.path(
        'recently_added/',
        feeds.views.RecentlyAddedMoviesView.as_view(),
        name='recently_added',
    ),
    django.urls.path(
        'best/',
        feeds.views.BestMoviesView.as_view(),
        name='best',
    ),
    django.urls.path(
        'search/',
        feeds.views.SearchView.as_view(),
        name='search',
    ),
]
