from smtplib import SMTPAuthenticationError

from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views import generic

from core.mixins import SearchViewMixin
from rating.models import Rating
from users.forms import ProfileForm, SignUpForm
from users.models import User
from users.tasks import send_email


class AccountActivationView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=self.kwargs['username'])
        if timezone.now() - user.date_joined > timezone.timedelta(weeks=1):
            raise Http404
        user.is_active = True
        user.save()

        return redirect(reverse_lazy('users:activation_done'))


class AccountActivationDoneView(generic.TemplateView):
    template_name = 'users/activation_done.html'


class ProfileView(generic.UpdateView):
    context_object_name = 'profile_owner'
    form_class = ProfileForm
    paginate_by = 10
    pk_url_kwarg = 'username'
    template_name = 'users/profile.html'

    def get_paginator(self):
        user = self.get_object()
        reviews = Rating.objects.get_review_by_user_id(user.id)
        paginator = Paginator(
            reviews,
            self.paginate_by,
        )
        page_obj = paginator.get_page(self.request.GET.get('page', 1))
        return paginator, page_obj

    def get_object(self):
        return get_object_or_404(
            User.objects.get_user_profile(),
            username=self.kwargs.get(self.pk_url_kwarg),
        )

    def get_success_url(self) -> str:
        return reverse_lazy(
            'users:profile',
            kwargs={
                self.pk_url_kwarg: self.object.username,
            },
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginator'], context['page_obj'] = self.get_paginator()
        return context


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = (
        '/'
        if settings.USERS_AUTOACTIVATE
        else reverse_lazy('users:signup_done')
    )
    template_name = 'users/signup.html'

    def send_email(self, user: User, absolute_uri: str):
        try:
            send_email.delay(user.username, user.email, absolute_uri)
        except SMTPAuthenticationError:
            user.is_active = True
            user.save()
            return redirect('/')

    def form_valid(self, form):
        user = form.save(commit=False)
        if not settings.USERS_AUTOACTIVATE:
            absolute_uri = self.request.build_absolute_uri(
                reverse_lazy('users:activation', args=[user.username])
            )
            self.send_email(user, absolute_uri)
        else:
            user.is_active = True
            user.save()
        return super().form_valid(form)


class SignUpDoneView(generic.TemplateView):
    template_name = 'users/signup_done.html'


class UserListView(generic.ListView):
    context_object_name = 'users'
    paginate_by = 30
    queryset = User.objects.all().order_by(
        User.username.field.name,
    )


class SearchView(generic.ListView, SearchViewMixin):
    context_object_name = 'users'
    paginate_by = 30

    def get_queryset(self):
        return User.objects.filter(
            username__icontains=self.request.GET.get('q')
        )
