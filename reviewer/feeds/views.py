import core.feeds.views
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


class SearchView(core.feeds.views.FeedBaseView):
    feed_name = 'search'

    def get_queryset(self):
        return movies.models.Movie.objects.filter(
            name__icontains=self.request.GET.get('q')
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
