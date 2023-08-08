import django.urls

import genres.views

app_name = 'genres'
urlpatterns = [
    django.urls.path(
        '',
        genres.views.GenreListView.as_view(),
        name='genres',
    ),
    django.urls.path(
        'search/',
        genres.views.SearchView.as_view(),
        name='search',
    ),
]
