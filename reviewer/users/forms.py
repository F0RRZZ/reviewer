from django.contrib.auth.forms import UserCreationForm
from django import forms

from core.mixins import BootstrapFormMixin
from users.models import User


class SignUpForm(
    BootstrapFormMixin,
    UserCreationForm,
):
    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            'password1',
            'password2',
        )


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    image = forms.ImageField(
        label='Avatar',
        required=False,
        error_messages={'invalid': 'Image files only'},
        widget=forms.FileInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[User.bio.field.name].required = False
        self.fields[User.email.field.name].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = (
            User.image.field.name,
            User.username.field.name,
            User.email.field.name,
            User.bio.field.name,
        )
