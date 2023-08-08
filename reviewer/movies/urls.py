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
    django.urls.path(
        '<int:movie_id>/actors/',
        movies.views.MovieActorsView.as_view(),
        name='movie_actors',
    ),
    django.urls.path(
        '<int:movie_id>/directors/',
        movies.views.MovieDirectorsView.as_view(),
        name='movie_directors',
    ),
    django.urls.path(
        '<int:movie_id>/producers/',
        movies.views.MovieProducersView.as_view(),
        name='movie_producers',
    ),
    django.urls.path(
        '<int:movie_id>/screenwriters/',
        movies.views.MovieScreenwritersView.as_view(),
        name='movie_screenwriters',
    ),
    django.urls.path(
        '<int:movie_id>/operators/',
        movies.views.MovieOperatorsView.as_view(),
        name='movie_operators',
    ),
    django.urls.path(
        '<int:movie_id>/composers/',
        movies.views.MovieComposersView.as_view(),
        name='movie_composers',
    ),
    django.urls.path(
        '<int:movie_id>/artists/',
        movies.views.MovieArtistsView.as_view(),
        name='movie_artists',
    ),
    django.urls.path(
        '<int:movie_id>/editors/',
        movies.views.MovieEditorsView.as_view(),
        name='movie_editors',
    ),
    django.urls.path(
        '<int:movie_id>/<str:staff_type>/search/',
        movies.views.SearchView.as_view(),
        name='search',
    ),
    django.urls.path(
        '<int:movie_id>/<str:staff_type>/search/',
        movies.views.SearchView.as_view(),
        name='search',
    ),
]
