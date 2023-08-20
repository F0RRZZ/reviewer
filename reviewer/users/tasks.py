from django.conf import settings
from django.core.mail import send_mail

from reviewer.celery import app


@app.task
def send_email(username: str, email: str, absolute_uri: str):
    send_mail(
        'Подтверждение регистрации',
        f'Здравствуйте, {username}!\n'
        f'Для активации аккаунта необходимо перейти'
        f'по ссылке: {absolute_uri}',
        settings.EMAIL,
        [email],
        fail_silently=False,
    )
