import django.contrib.auth.forms
import django.forms

import core.mixins
import users.models


class SignUpForm(
    core.mixins.BootstrapFormMixin,
    django.contrib.auth.forms.UserCreationForm,
):
    class Meta:
        model = users.models.User
        fields = (
            users.models.User.username.field.name,
            users.models.User.email.field.name,
            'password1',
            'password2',
        )


class ProfileForm(core.mixins.BootstrapFormMixin, django.forms.ModelForm):
    image = django.forms.ImageField(
        label='Avatar',
        required=False,
        error_messages={'invalid': 'Image files only'},
        widget=django.forms.FileInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[users.models.User.bio.field.name].required = False
        self.fields[users.models.User.email.field.name].widget.attrs[
            'readonly'
        ] = True

    class Meta:
        model = users.models.User
        fields = (
            users.models.User.image.field.name,
            users.models.User.username.field.name,
            users.models.User.email.field.name,
            users.models.User.bio.field.name,
        )
