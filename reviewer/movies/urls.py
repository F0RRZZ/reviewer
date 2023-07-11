import django.urls

import movies.views

app_name = 'movies'
urlpatterns = [
    django.urls.path(
        '<str:genre>/',
        movies.views.MoviesByGenreView.as_view(),
        name='movies_by_genre',
    ),
]
