from django.urls import path

from movies import views

app_name = 'movies'
urlpatterns = [
    path(
        'genre/<str:genre>/',
        views.MoviesByGenreView.as_view(),
        name='movies_by_genre',
    ),
    path(
        'detail/<int:movie_id>/',
        views.MovieDetailView.as_view(),
        name='movie_detail',
    ),
    path(
        '<int:movie_id>/actors/',
        views.MovieActorsView.as_view(),
        name='movie_actors',
    ),
    path(
        '<int:movie_id>/directors/',
        views.MovieDirectorsView.as_view(),
        name='movie_directors',
    ),
    path(
        '<int:movie_id>/producers/',
        views.MovieProducersView.as_view(),
        name='movie_producers',
    ),
    path(
        '<int:movie_id>/screenwriters/',
        views.MovieScreenwritersView.as_view(),
        name='movie_screenwriters',
    ),
    path(
        '<int:movie_id>/operators/',
        views.MovieOperatorsView.as_view(),
        name='movie_operators',
    ),
    path(
        '<int:movie_id>/composers/',
        views.MovieComposersView.as_view(),
        name='movie_composers',
    ),
    path(
        '<int:movie_id>/artists/',
        views.MovieArtistsView.as_view(),
        name='movie_artists',
    ),
    path(
        '<int:movie_id>/editors/',
        views.MovieEditorsView.as_view(),
        name='movie_editors',
    ),
    path(
        '<int:movie_id>/<str:staff_type>/search/',
        views.SearchView.as_view(),
        name='search',
    ),
    path(
        '<int:movie_id>/<str:staff_type>/search/',
        views.SearchView.as_view(),
        name='search',
    ),
]
