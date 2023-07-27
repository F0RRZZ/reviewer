import django.db.models
import django.db.models.fields
import django.db.models.functions

import genres.models
import movies.models


class MovieManager(django.db.models.Manager):
    def get_with_genres(self):
        return self.get_queryset().prefetch_related(
            django.db.models.Prefetch(
                movies.models.Movie.genre.field.name,
                queryset=genres.models.Genre.objects.only(
                    movies.models.Movie.name.field.name,
                ),
            )
        )

    def get_new_movies(self):
        return self.get_with_genres().order_by(
            f'-{movies.models.Movie.created_at.field.name}'
        )

    def get_recently_added_movies(self):
        return self.get_with_genres().order_by(
            f'-{movies.models.Movie.uploaded_at.field.name}'
        )

    def get_best_movies(self):
        return (
            self.get_with_genres()
            .annotate(
                avg_rating=django.db.models.functions.Coalesce(
                    django.db.models.Avg('score_movie__total_rating'),
                    django.db.models.Value(0),
                    output_field=django.db.models.fields.FloatField(),
                )
            )
            .order_by('-avg_rating')
        )

    def get_for_view_details(self):
        return self.get_with_genres().prefetch_related(
            movies.models.Movie.actors.field.name,
            movies.models.Movie.director.field.name,
            movies.models.Movie.producer.field.name,
            movies.models.Movie.screenwriter.field.name,
            movies.models.Movie.operator.field.name,
            movies.models.Movie.composer.field.name,
            movies.models.Movie.artist.field.name,
            movies.models.Movie.montage.field.name,
        )
