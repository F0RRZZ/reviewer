from django.core.validators import ValidationError
from django.db.models import Model

from core.tools import name_formatter


class NameFormatterBaseModel(Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.formatted_name = name_formatter(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        formatted_name = name_formatter(self.name)
        if self.__class__.objects.filter(
            formatted_name=formatted_name
        ).exists():
            raise ValidationError('Name must be unique')
        return self.name
