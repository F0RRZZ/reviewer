import django.views.generic

import movies.models


class NewMoviesView(django.views.generic.ListView):
    paginate_by = 5
    template_name = 'feeds/feed.html'
    queryset = movies.models.Movie.objects.new_movies()
