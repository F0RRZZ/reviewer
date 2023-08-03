import django.core.paginator
import django.shortcuts
import django.urls
import django.views.generic

import movies.models
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
        context = super().get_context_data(**kwargs)
        movie = self.object
        review = self.get_review()
        context['movie'] = movie
        context['review_exists'] = review is not None
        context['paginator'], context['page_obj'] = self.get_paginator()
        context['avg_total_rating'] = rating.models.Rating.objects.get_avg(
            movie.id, rating.models.Rating.total_rating.field.name
        )
        context['avg_story_rating'] = rating.models.Rating.objects.get_avg(
            movie.id, rating.models.Rating.story.field.name
        )
        context['avg_acting_rating'] = rating.models.Rating.objects.get_avg(
            movie.id,
            rating.models.Rating.acting.field.name,
        )
        context['avg_music_rating'] = rating.models.Rating.objects.get_avg(
            movie.id,
            rating.models.Rating.music.field.name,
        )
        context['avg_visual_rating'] = rating.models.Rating.objects.get_avg(
            movie.id,
            rating.models.Rating.visual.field.name,
        )
        context['avg_final_rating'] = rating.models.Rating.objects.get_avg(
            movie.id,
            rating.models.Rating.final.field.name,
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
