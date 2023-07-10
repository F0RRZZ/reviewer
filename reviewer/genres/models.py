import django.db.models

import core.base_models


class Genre(core.base_models.NameFormatterBaseModel):
    name = django.db.models.CharField(
        'name',
        max_length=50,
        help_text='Maximum of 50 symbols',
    )
    formatted_name = django.db.models.CharField(
        'formatted_name',
        max_length=50,
    )

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name[:30]
