import django.urls

import movies.views

app_name = 'movies'
urlpatterns = [
    django.urls.path(
        'genre/<str:genre>/',
        movies.views.MoviesByGenreView.as_view(),
        name='movies_by_genre',
    ),
    django.urls.path(
        'detail/<int:movie_id>/',
        movies.views.MovieDetailView.as_view(),
        name='movie_detail',
    ),
]
