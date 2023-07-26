import os

import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviewer.settings')

app = celery.Celery('reviewer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
