import django.views.generic
import django.urls

import users.forms


class SignUpView(django.views.generic.CreateView):
    template_name = 'users/signup.html'
    form_class = users.forms.SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        return super().form_valid(form)
