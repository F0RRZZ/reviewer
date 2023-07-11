import django.core.validators
import django.db.models

import movies.models
import users.models


class Rating(django.db.models.Model):
    class ScoreData:
        DEFAULT = 5
        MIN = 1
        MAX = 10
        VALIDATORS = [
            django.core.validators.MinValueValidator(MIN),
            django.core.validators.MaxValueValidator(MAX),
        ]

    movie = django.db.models.ForeignKey(
        movies.models.Movie,
        on_delete=django.db.models.CASCADE,
        related_name='score_movie',
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='score_user',
    )
    story = django.db.models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    acting = django.db.models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    music = django.db.models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    visual = django.db.models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    final = django.db.models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    total_rating = django.db.models.PositiveSmallIntegerField('total_rating')
    comment = django.db.models.TextField(
        'comment',
        max_length=1000,
        help_text='Maximum of 1000 symbols',
        null=True,
    )

    class Meta:
        verbose_name = 'rating'
        verbose_name_plural = 'ratings'

    def save(self, *args, **kwargs):
        self.total_rating = (
            self.story + self.acting + self.music + self.visual + self.final
        ) / 5
        return super().save(*args, **kwargs)
