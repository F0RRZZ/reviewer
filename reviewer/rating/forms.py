import django.forms

import core.mixins
import rating.models


class RatingForm(core.mixins.BootstrapFormMixin, django.forms.ModelForm):
    class Meta:
        model = rating.models.Rating
        fields = [
            rating.models.Rating.story.field.name,
            rating.models.Rating.acting.field.name,
            rating.models.Rating.music.field.name,
            rating.models.Rating.visual.field.name,
            rating.models.Rating.final.field.name,
            rating.models.Rating.comment.field.name,
        ]
        labels = {
            rating.models.Rating.story.field.name: 'Story',
            rating.models.Rating.acting.field.name: 'Acting',
            rating.models.Rating.music.field.name: 'Music',
            rating.models.Rating.visual.field.name: 'Visual',
            rating.models.Rating.final.field.name: 'Final',
            rating.models.Rating.comment.field.name: 'Comment',
        }
        widgets = {
            rating.models.Rating.story.field.name: django.forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        rating.models.Rating.story.field.name
                    ),
                }
            ),
            rating.models.Rating.acting.field.name: django.forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        rating.models.Rating.acting.field.name
                    ),
                }
            ),
            rating.models.Rating.visual.field.name: django.forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        rating.models.Rating.visual.field.name
                    ),
                }
            ),
            rating.models.Rating.music.field.name: django.forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        rating.models.Rating.music.field.name
                    ),
                }
            ),
            rating.models.Rating.final.field.name: django.forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        rating.models.Rating.final.field.name
                    ),
                }
            ),
        }
