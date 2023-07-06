import django.contrib.auth.views
import django.urls

app_name = 'users'
urlpatterns = [
    django.urls.path(
        'login/',
        django.contrib.auth.views.LoginView.as_view(
            template_name='users/login.html'
        ),
        name='login',
    ),
    django.urls.path(
        'logout/',
        django.contrib.auth.views.LogoutView.as_view(),
        name='logout',
    ),
    django.urls.path(
        'change_password/',
        django.contrib.auth.views.PasswordChangeView.as_view(
            template_name='users/change_password.html'
        ),
        name='change_password',
    ),
    django.urls.path(
        'change_password/done/',
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name='users/change_password_done.html',
        ),
        name='change_password_done',
    ),
    django.urls.path(
        'reset_password/',
        django.contrib.auth.views.PasswordResetView.as_view(
            template_name='users/reset_password.html',
        ),
        name='reset_password',
    ),
    django.urls.path(
        'reset_password/done/',
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name='users/reset_password_done.html',
        ),
        name='reset_password_done',
    ),
    django.urls.path(
        'reset/<uidb64>/<token>/',
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name='users/reset_password_confirm.html',
        ),
        name='reset_password_confirm',
    ),
    django.urls.path(
        'reset/done/',
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name='users/reset_password_complete.html',
        ),
        name='reset_password_complete',
    ),
]