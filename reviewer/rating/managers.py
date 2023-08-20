from django.db import models

import rating.models


class RatingManager(models.Manager):
    def get_avg(self, movie_id: int, evaluation_parameter: str):
        avg = (
            self.filter(movie_id=movie_id)
            .aggregate(
                avg=models.Avg(
                    evaluation_parameter,
                )
            )
            .get('avg')
        )
        if avg is None:
            return 0
        return round(avg, 1)

    def get_review_with_movie_and_user(self):
        return self.prefetch_related(
            rating.models.Rating.movie.field.name,
            rating.models.Rating.user.field.name,
        )

    def get_review_by_user_id(self, user_id: int):
        return self.get_review_with_movie_and_user().filter(user_id=user_id)
