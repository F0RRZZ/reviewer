from django.db.models import Avg, Manager, Prefetch, Value
from django.db.models.fields import FloatField
from django.db.models.functions import Coalesce

from genres.models import Genre
import movies.models


class MovieManager(Manager):
    def get_with_genres(self):
        return self.get_queryset().prefetch_related(
            Prefetch(
                movies.models.Movie.genre.field.name,
                queryset=Genre.objects.only(
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
                avg_rating=Coalesce(
                    Avg('movies_reviews__total_rating'),
                    Value(0),
                    output_field=FloatField(),
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
            movies.models.Movie.genre.field.name,
        )
