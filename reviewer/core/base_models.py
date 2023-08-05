import django.core.validators
import django.db.models

import core.tools


class NameFormatterBaseModel(django.db.models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.formatted_name = core.tools.name_formatter(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        formatted_name = core.tools.name_formatter(self.name)
        if self.__class__.objects.filter(
            formatted_name=formatted_name
        ).exists():
            raise django.core.validators.ValidationError('Name must be unique')
        return self.name
