from core.feeds.views import FeedBaseView
from core.mixins import SearchViewMixin
from movies.models import Movie


class BestMoviesView(FeedBaseView):
    feed_name = 'best'
    queryset = Movie.objects.get_best_movies()


class NewMoviesView(FeedBaseView):
    feed_name = 'new'
    queryset = Movie.objects.get_new_movies()


class RecentlyAddedMoviesView(FeedBaseView):
    feed_name = 'recently added'
    queryset = Movie.objects.get_recently_added_movies()


class SearchView(FeedBaseView, SearchViewMixin):
    feed_name = 'search'

    def get_queryset(self):
        return Movie.objects.filter(name__icontains=self.request.GET.get('q'))
