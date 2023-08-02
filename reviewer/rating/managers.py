import django.db.models


class RatingManager(django.db.models.Manager):
    def get_avg(self, movie_id: int, evaluation_parameter: str):
        avg = (
            self.filter(movie_id=movie_id)
            .aggregate(
                avg=django.db.models.Avg(
                    evaluation_parameter,
                )
            )
            .get('avg')
        )
        if avg is None:
            return 0
        return round(avg, 1)
