import os
from celery import Celery

# Set default settings module for 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myworld.settings")

app = Celery("myworld")

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in Django apps
app.autodiscover_tasks()
