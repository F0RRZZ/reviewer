import core.feeds.views
import movies.models


class NewMoviesView(core.feeds.views.FeedBaseView):
    feed_name = 'new'
    queryset = movies.models.Movie.objects.new_movies()


class RecentlyAddedMoviesView(core.feeds.views.FeedBaseView):
    feed_name = 'recently_added'
    queryset = movies.models.Movie.objects.recently_added_movies()


class BestMoviesView(core.feeds.views.FeedBaseView):
    ...
