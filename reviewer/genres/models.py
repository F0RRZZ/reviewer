from django.db import models

from core.base_models import NameFormatterBaseModel


class Genre(NameFormatterBaseModel):
    name = models.CharField(
        'name',
        max_length=50,
        help_text='Maximum of 50 symbols',
    )
    formatted_name = models.CharField(
        'formatted_name',
        max_length=50,
    )

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name[:30]
