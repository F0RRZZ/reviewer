import django.urls

import feeds.views

app_name = 'feeds'
urlpatterns = [
    django.urls.path(
        '',
        feeds.views.NewMoviesView.as_view(),
    ),
    django.urls.path(
        'new/',
        feeds.views.NewMoviesView.as_view(),
    ),
    django.urls.path(
        'recently_added/',
        feeds.views.RecentlyAddedMoviesView.as_view(),
    ),
    django.urls.path(
        'best/',
        feeds.views.BestMoviesView.as_view(),
    ),
]
