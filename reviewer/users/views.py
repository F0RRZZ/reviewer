import smtplib

import django.conf
import django.core.mail
import django.core.paginator
import django.http
import django.shortcuts
import django.urls
import django.utils.timezone
import django.views
import django.views.generic

import rating.models
import users.forms
import users.models
import users.tasks


class AccountActivationView(django.views.View):
    def get(self, request, *args, **kwargs):
        user = django.shortcuts.get_object_or_404(
            users.models.User, username=self.kwargs['username']
        )
        if (
            django.utils.timezone.now() - user.date_joined
            > django.utils.timezone.timedelta(weeks=1)
        ):
            raise django.http.Http404
        user.is_active = True
        user.save()

        return django.shortcuts.redirect(
            django.urls.reverse_lazy('users:activation_done')
        )


class AccountActivationDoneView(
    django.views.generic.TemplateView,
):
    template_name = 'users/activation_done.html'


class ProfileView(django.views.generic.UpdateView):
    context_object_name = 'profile_owner'
    form_class = users.forms.ProfileForm
    paginate_by = 10
    pk_url_kwarg = 'username'
    template_name = 'users/profile.html'

    def get_paginator(self):
        user = self.get_object()
        reviews = (
            rating.models.Rating.objects
            .prefetch_related(rating.models.Rating.movie.field.name)
            .filter(user_id=user.id)
        )
        paginator = django.core.paginator.Paginator(
            reviews,
            self.paginate_by,
        )
        page_obj = paginator.get_page(self.request.GET.get('page', 1))
        return paginator, page_obj

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginator'], context['page_obj'] = self.get_paginator()
        return context


class SignUpView(django.views.generic.CreateView):
    form_class = users.forms.SignUpForm
    success_url = (
        '/'
        if django.conf.settings.USERS_AUTOACTIVATE
        else django.urls.reverse_lazy('users:signup_done')
    )
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        if not django.conf.settings.USERS_AUTOACTIVATE:
            absolute_uri = self.request.build_absolute_uri(
                django.urls.reverse_lazy(
                    'users:activation', args=[user.username]
                )
            )
            try:
                users.tasks.send_email.delay(
                    user.username, user.email, absolute_uri
                )
            except smtplib.SMTPAuthenticationError:
                user.is_active = True
                user.save()
                return django.shortcuts.redirect('/')
        else:
            user.is_active = True
            user.save()
        return super().form_valid(form)


class SignUpDoneView(
    django.views.generic.TemplateView,
):
    template_name = 'users/signup_done.html'


class UserListView(django.views.generic.ListView):
    context_object_name = 'users'
    paginate_by = 30
    queryset = users.models.User.objects.all().order_by(
        users.models.User.username.field.name,
    )
