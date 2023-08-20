from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie
from rating.managers import RatingManager
from users.models import User


class Rating(models.Model):
    class ScoreData:
        DEFAULT = 5
        MIN = 1
        MAX = 10
        VALIDATORS = [
            MinValueValidator(MIN),
            MaxValueValidator(MAX),
        ]

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='movies_reviews',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users_reviews',
    )
    story = models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    acting = models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    music = models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    visual = models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    final = models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        validators=ScoreData.VALIDATORS,
    )
    total_rating = models.PositiveSmallIntegerField('total_rating')
    comment = models.TextField(
        'comment',
        max_length=1000,
        help_text='Maximum of 1000 symbols',
        null=True,
    )
    created_at = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        null=True,
    )

    objects = RatingManager()

    class Meta:
        verbose_name = 'rating'
        verbose_name_plural = 'ratings'

    def __str__(self):
        return 'Rating'

    def save(self, *args, **kwargs):
        self.total_rating = (
            self.story + self.acting + self.music + self.visual + self.final
        ) / 5
        return super().save(*args, **kwargs)
