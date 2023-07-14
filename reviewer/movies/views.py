import django.core.paginator
import django.views.generic

import movies.models
import rating.models


class MovieDetailView(django.views.generic.DetailView):
    paginate_by = 20
    pk_url_kwarg = 'movie_id'
    queryset = movies.models.Movie.objects.get_for_view_details()
    template_name = 'movies/movie_detail.html'

    def is_review_exists(self):
        try:
            rating.models.Rating.objects.get(
                user_id=self.request.user.id,
                movie_id=self.kwargs[self.pk_url_kwarg],
            )
            return True
        except rating.models.Rating.DoesNotExist:
            return False

    def get_paginator(self):
        reviews = rating.models.Rating.objects.select_related('user').filter(
            movie_id=self.kwargs[self.pk_url_kwarg]
        )
        paginator = django.core.paginator.Paginator(
            reviews,
            self.paginate_by,
        )
        page_obj = paginator.get_page(self.request.GET.get('page', 1))
        return paginator, page_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        review_exists = self.is_review_exists()
        context['movie'] = movie
        context['review_exists'] = review_exists
        context['paginator'], context['page_obj'] = self.get_paginator()
        context['avg_rating'] = rating.models.Rating.objects.get_avg(movie.id)
        return context


class MoviesByGenreView(django.views.generic.ListView):
    context_object_name = 'movies'
    model = movies.models.Movie
    paginate_by = 12
    template_name = 'movies/movies_by_genre.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('genre').filter(
            genre__name=self.kwargs.get('genre')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = self.kwargs.get('genre')
        return context
