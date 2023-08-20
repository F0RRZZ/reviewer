from django.urls import path

from feeds import views

app_name = 'feeds'
urlpatterns = [
    path(
        '',
        views.NewMoviesView.as_view(),
        name='new',
    ),
    path(
        'new/',
        views.NewMoviesView.as_view(),
        name='new',
    ),
    path(
        'recently_added/',
        views.RecentlyAddedMoviesView.as_view(),
        name='recently_added',
    ),
    path(
        'best/',
        views.BestMoviesView.as_view(),
        name='best',
    ),
    path(
        'search/',
        views.SearchView.as_view(),
        name='search',
    ),
]
