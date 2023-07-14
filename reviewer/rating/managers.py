import django.db.models

import rating.models


class RatingManager(django.db.models.Manager):
    def get_avg(self, movie_id):
        avg = (
            self.filter(movie_id=movie_id)
            .aggregate(
                avg=django.db.models.Avg(
                    rating.models.Rating.total_rating.field.name,
                )
            )
            .get('avg')
        )
        if avg is None:
            return 0
        return round(avg, 1)
