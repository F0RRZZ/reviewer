from django.urls import path

from genres.views import GenreListView, SearchView

app_name = 'genres'
urlpatterns = [
    path(
        '',
        GenreListView.as_view(),
        name='genres',
    ),
    path(
        'search/',
        SearchView.as_view(),
        name='search',
    ),
]
