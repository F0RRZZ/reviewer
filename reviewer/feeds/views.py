import core.feeds.views
import core.mixins
import movies.models


class BestMoviesView(core.feeds.views.FeedBaseView):
    feed_name = 'best'
    queryset = movies.models.Movie.objects.get_best_movies()


class NewMoviesView(core.feeds.views.FeedBaseView):
    feed_name = 'new'
    queryset = movies.models.Movie.objects.get_new_movies()


class RecentlyAddedMoviesView(core.feeds.views.FeedBaseView):
    feed_name = 'recently added'
    queryset = movies.models.Movie.objects.get_recently_added_movies()


class SearchView(core.feeds.views.FeedBaseView, core.mixins.SearchViewMixin):
    feed_name = 'search'

    def get_queryset(self):
        return movies.models.Movie.objects.filter(
            name__icontains=self.request.GET.get('q')
        )
