import django.db.models

import movies.models


class MovieManager(django.db.models.Manager):
    def new_movies(self):
        return self.get_queryset().order_by(
            f'-{movies.models.Movie.uploaded_at.field.name}'
        )
