from django import forms

from core.mixins import BootstrapFormMixin
from rating.models import Rating


class RatingForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            Rating.story.field.name,
            Rating.acting.field.name,
            Rating.music.field.name,
            Rating.visual.field.name,
            Rating.final.field.name,
            Rating.comment.field.name,
        ]
        labels = {
            Rating.story.field.name: 'Story',
            Rating.acting.field.name: 'Acting',
            Rating.music.field.name: 'Music',
            Rating.visual.field.name: 'Visual',
            Rating.final.field.name: 'Final',
            Rating.comment.field.name: 'Comment',
        }
        widgets = {
            Rating.story.field.name: forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        Rating.story.field.name
                    ),
                }
            ),
            Rating.acting.field.name: forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        Rating.acting.field.name
                    ),
                }
            ),
            Rating.visual.field.name: forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        Rating.visual.field.name
                    ),
                }
            ),
            Rating.music.field.name: forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        Rating.music.field.name
                    ),
                }
            ),
            Rating.final.field.name: forms.TextInput(
                attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '10',
                    'class': 'form-range',
                    'oninput': 'updateValue("{}")'.format(
                        Rating.final.field.name
                    ),
                }
            ),
        }
