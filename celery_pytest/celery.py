import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_pytest.settings')


app = Celery("celery_pytest")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
