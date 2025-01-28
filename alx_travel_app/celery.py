from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

# Create an instance of Celery
app = Celery('alx_travel_app')

# Load task-related settings from Django's settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
