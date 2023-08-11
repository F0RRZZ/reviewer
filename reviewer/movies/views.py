import django.core.paginator
import django.db.models
import django.shortcuts
import django.urls
import django.views.generic

import core.mixins
import core.movies.views
import movies.models
import persons.models
import rating.forms
import rating.models


class MovieDetailView(django.views.generic.DetailView):
    paginate_by = 20
    pk_url_kwarg = 'movie_id'
    queryset = movies.models.Movie.objects.get_for_view_details()
    template_name = 'movies/movie_detail.html'

    def get_review(self):
        try:
            review = rating.models.Rating.objects.get(
                user_id=self.request.user.id,
                movie_id=self.kwargs[self.pk_url_kwarg],
            )
            return review
        except rating.models.Rating.DoesNotExist:
            return None

    def get_review_form_initial_data(self, review=None) -> dict:
        if not review:
            review = rating.models.Rating(
                user_id=self.request.user.id,
                movie_id=self.kwargs[self.pk_url_kwarg],
                story=rating.models.Rating.ScoreData.DEFAULT,
                acting=rating.models.Rating.ScoreData.DEFAULT,
                music=rating.models.Rating.ScoreData.DEFAULT,
                visual=rating.models.Rating.ScoreData.DEFAULT,
                final=rating.models.Rating.ScoreData.DEFAULT,
            )
        initial = {
            rating.models.Rating.story.field.name: review.story,
            rating.models.Rating.acting.field.name: review.acting,
            rating.models.Rating.music.field.name: review.music,
            rating.models.Rating.visual.field.name: review.visual,
            rating.models.Rating.final.field.name: review.final,
            rating.models.Rating.comment.field.name: review.comment,
        }
        return initial

    def get_paginator(self):
        reviews = rating.models.Rating.objects.select_related(
            rating.models.Rating.user.field.name
        ).filter(movie_id=self.kwargs[self.pk_url_kwarg])
        paginator = django.core.paginator.Paginator(
            reviews,
            self.paginate_by,
        )
        page_obj = paginator.get_page(self.request.GET.get('page', 1))
        return paginator, page_obj

    def get_context_data(self, **kwargs):
        fields = [
            rating.models.Rating.story.field.name,
            rating.models.Rating.acting.field.name,
            rating.models.Rating.music.field.name,
            rating.models.Rating.visual.field.name,
            rating.models.Rating.final.field.name,
        ]
        context = super().get_context_data(**kwargs)
        movie = self.object
        review = self.get_review()
        context['movie'] = movie
        context['review_exists'] = review is not None
        context['paginator'], context['page_obj'] = self.get_paginator()
        for field in fields:
            context[
                f'avg_{field}_rating'
            ] = rating.models.Rating.objects.get_avg(
                movie.id,
                field,
            )
        context['form'] = rating.forms.RatingForm(
            initial=self.get_review_form_initial_data(review=review)
        )
        return context

    def post(self, request, movie_id):
        existing_review = rating.models.Rating.objects.filter(
            user_id=request.user.id,
            movie_id=self.kwargs[self.pk_url_kwarg],
        ).first()

        review_form = rating.forms.RatingForm(
            request.POST or None, instance=existing_review
        )
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user_id = request.user.id
            review.movie_id = movie_id
            review.save()

        return django.shortcuts.redirect(
            django.urls.reverse_lazy('movies:movie_detail', kwargs=self.kwargs)
        )


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


class MovieActorsView(core.movies.views.BaseMovieStaffWithModifiedContextData):
    staff_type = 'actors'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        actors = persons.models.Person.objects.filter(actors__in=[movie.id])
        return actors


class MovieDirectorsView(
    core.movies.views.BaseMovieStaffWithModifiedContextData
):
    staff_type = 'directors'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        directors = persons.models.Person.objects.filter(
            director__in=[movie.id]
        )
        return directors


class MovieProducersView(
    core.movies.views.BaseMovieStaffWithModifiedContextData
):
    staff_type = 'producers'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        producers = persons.models.Person.objects.filter(
            producer__in=[movie.id]
        )
        return producers


class MovieScreenwritersView(
    core.movies.views.BaseMovieStaffWithModifiedContextData
):
    staff_type = 'screenwriters'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        screenwriters = persons.models.Person.objects.filter(
            screenwriter__in=[movie.id]
        )
        return screenwriters


class MovieOperatorsView(
    core.movies.views.BaseMovieStaffWithModifiedContextData
):
    staff_type = 'operators'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        operators = persons.models.Person.objects.filter(
            operator__in=[movie.id]
        )
        return operators


class MovieComposersView(
    core.movies.views.BaseMovieStaffWithModifiedContextData
):
    staff_type = 'composers'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        composers = persons.models.Person.objects.filter(
            composer__in=[movie.id]
        )
        return composers


class MovieArtistsView(
    core.movies.views.BaseMovieStaffWithModifiedContextData
):
    staff_type = 'artists'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        artists = persons.models.Person.objects.filter(artist__in=[movie.id])
        return artists


class MovieEditorsView(
    core.movies.views.BaseMovieStaffWithModifiedContextData
):
    staff_type = 'editors'

    def get_queryset(self):
        movie = movies.models.Movie.objects.filter(
            pk=self.kwargs[self.pk_url_kwarg]
        ).first()
        editors = persons.models.Person.objects.filter(montage__in=[movie.id])
        return editors


class SearchView(
    core.movies.views.BaseMovieStaffView, core.mixins.SearchViewMixin
):
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
            django.db.models.Q(name__icontains=self.request.GET.get('q'))
            | django.db.models.Q(surname__icontains=self.request.GET.get('q'))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['movie_id'] = self.kwargs[self.pk_url_kwarg]
        context['staff_type'] = self.kwargs['staff_type']
        return context
