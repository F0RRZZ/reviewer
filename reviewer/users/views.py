import django.shortcuts
import django.urls
import django.views.generic

import users.forms
import users.models


class SignUpView(django.views.generic.CreateView):
    form_class = users.forms.SignUpForm
    success_url = '/'
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        return super().form_valid(form)


class ProfileView(django.views.generic.UpdateView):
    context_object_name = 'profile_owner'
    form_class = users.forms.ProfileForm
    pk_url_kwarg = 'username'
    template_name = 'users/profile.html'

    def get_object(self):
        return django.shortcuts.get_object_or_404(
            users.models.User.objects.get_user_profile(),
            username=self.kwargs.get(self.pk_url_kwarg),
        )

    def get_success_url(self) -> str:
        return django.urls.reverse_lazy(
            'users:profile',
            kwargs={
                self.pk_url_kwarg: self.object.username,
            },
        )
