from django.db.models import CharField

from core.base_models import NameFormatterBaseModel


class Role(NameFormatterBaseModel):
    name = CharField(
        'name',
        max_length=50,
        help_text='Maximum of 50 symbols',
    )
    formatted_name = CharField(
        'formatted_name',
        max_length=50,
    )

    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.name[:30]
