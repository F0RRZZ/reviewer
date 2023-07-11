import django.views.generic

import movies.models


class MovieDetailView(django.views.generic.ListView):
    ...


class MoviesByGenreView(django.views.generic.ListView):
    context_object_name = 'movies'
    model = movies.models.Movie
    paginate_by = 12
    template_name = 'movies/movies_by_genre.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(genre__name=self.kwargs.get('genre'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = self.kwargs.get('genre')
        return context
