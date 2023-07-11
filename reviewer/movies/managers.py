import django.db.models

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

    def new_movies(self):
        return self.get_with_genres().order_by(
            f'-{movies.models.Movie.created_at.field.name}'
        )

    def recently_added_movies(self):
        return self.get_with_genres().order_by(
            f'-{movies.models.Movie.uploaded_at.field.name}'
        )
