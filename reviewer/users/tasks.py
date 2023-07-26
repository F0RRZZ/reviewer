import django.conf
import django.core.mail

import reviewer.celery


@reviewer.celery.app.task
def send_email(username: str, email: str, absolute_uri: str):
    django.core.mail.send_mail(
        'Подтверждение регистрации',
        f'Здравствуйте, {username}!\n'
        f'Для активации аккаунта необходимо перейти'
        f'по ссылке: {absolute_uri}',
        django.conf.settings.EMAIL,
        [email],
        fail_silently=False,
    )
