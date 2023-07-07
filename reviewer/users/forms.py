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
