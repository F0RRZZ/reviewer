from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from core.mixins import SearchViewMixin
from core.movies.views import (
    BaseMovieStaffWithModifiedContextData,
    BaseMovieStaffView,
)
from movies.models import Movie
from persons.models import Person
from rating.forms import RatingForm
from rating.models import Rating


class MovieDetailView(DetailView):
    paginate_by = 20
    pk_url_kwarg = 'movie_id'
    queryset = Movie.objects.get_for_view_details()
    template_name = 'movies/movie_detail.html'

    def get_review(self):
        try:
            review = Rating.objects.get(
                user_id=self.request.user.id,
                movie_id=self.kwargs[self.pk_url_kwarg],
            )
            return review
        except Rating.DoesNotExist:
            return None

    def get_review_form_initial_data(self, review=None) -> dict:
        if not review:
            review = Rating(
                user_id=self.request.user.id,
                movie_id=self.kwargs[self.pk_url_kwarg],
                story=Rating.ScoreData.DEFAULT,
                acting=Rating.ScoreData.DEFAULT,
                music=Rating.ScoreData.DEFAULT,
                visual=Rating.ScoreData.DEFAULT,
                final=Rating.ScoreData.DEFAULT,
            )
        initial = {
            Rating.story.field.name: review.story,
            Rating.acting.field.name: review.acting,
            Rating.music.field.name: review.music,
            Rating.visual.field.name: review.visual,
            Rating.final.field.name: review.final,
            Rating.comment.field.name: review.comment,
        }
        return initial

    def get_paginator(self):
        reviews = Rating.objects.select_related(Rating.user.field.name).filter(
            movie_id=self.kwargs[self.pk_url_kwarg]
        )
        paginator = Paginator(
            reviews,
            self.paginate_by,
        )
        page_obj = paginator.get_page(self.request.GET.get('page', 1))
        return paginator, page_obj

    def get_context_data(self, **kwargs):
        fields = [
            Rating.story.field.name,
            Rating.acting.field.name,
            Rating.music.field.name,
            Rating.visual.field.name,
            Rating.final.field.name,
        ]
        context = super().get_context_data(**kwargs)
        movie = self.object
        review = self.get_review()
        context['movie'] = movie
        context['review_exists'] = review is not None
        context['paginator'], context['page_obj'] = self.get_paginator()
        for field in fields:
            context[f'avg_{field}_rating'] = Rating.objects.get_avg(
                movie.id,
                field,
            )
        context['form'] = RatingForm(
            initial=self.get_review_form_initial_data(review=review)
        )
        return context

    def post(self, request, movie_id):
        existing_review = Rating.objects.filter(
            user_id=request.user.id,
            movie_id=self.kwargs[self.pk_url_kwarg],
        ).first()

        review_form = RatingForm(
            request.POST or None, instance=existing_review
        )
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user_id = request.user.id
            review.movie_id = movie_id
            review.save()

        return redirect(
            reverse_lazy('movies:movie_detail', kwargs=self.kwargs)
        )


class MoviesByGenreView(ListView):
    context_object_name = 'movies'
    model = Movie
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


class MovieActorsView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'actors'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        actors = Person.objects.filter(actors__in=[movie.id])
        return actors


class MovieDirectorsView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'directors'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        directors = Person.objects.filter(director__in=[movie.id])
        return directors


class MovieProducersView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'producers'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        producers = Person.objects.filter(producer__in=[movie.id])
        return producers


class MovieScreenwritersView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'screenwriters'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        screenwriters = Person.objects.filter(screenwriter__in=[movie.id])
        return screenwriters


class MovieOperatorsView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'operators'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        operators = Person.objects.filter(operator__in=[movie.id])
        return operators


class MovieComposersView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'composers'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        composers = Person.objects.filter(composer__in=[movie.id])
        return composers


class MovieArtistsView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'artists'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        artists = Person.objects.filter(artist__in=[movie.id])
        return artists


class MovieEditorsView(BaseMovieStaffWithModifiedContextData):
    staff_type = 'editors'

    def get_queryset(self):
        movie = Movie.objects.filter(pk=self.kwargs[self.pk_url_kwarg]).first()
        editors = Person.objects.filter(montage__in=[movie.id])
        return editors


class SearchView(BaseMovieStaffView, SearchViewMixin):
    def get_queryset(self):
        staff_type = self.kwargs['staff_type']
        queryset = None
        if staff_type == 'actors':
            queryset = MovieActorsView.get_queryset(self)
        if staff_type == 'directors':
            queryset = MovieDirectorsView.get_queryset(self)
        if staff_type == 'producers':
            queryset = MovieProducersView.get_queryset(self)
        if staff_type == 'screenwriters':
            queryset = MovieScreenwritersView.get_queryset(self)
        if staff_type == 'operators':
            queryset = MovieOperatorsView.get_queryset(self)
        if staff_type == 'composers':
            queryset = MovieComposersView.get_queryset(self)
        if staff_type == 'artists':
            queryset = MovieArtistsView.get_queryset(self)
        if staff_type == 'editors':
            queryset = MovieEditorsView.get_queryset(self)
        return queryset.filter(
            Q(name__icontains=self.request.GET.get('q'))
            | Q(surname__icontains=self.request.GET.get('q'))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['movie_id'] = self.kwargs[self.pk_url_kwarg]
        context['staff_type'] = self.kwargs['staff_type']
        return context
