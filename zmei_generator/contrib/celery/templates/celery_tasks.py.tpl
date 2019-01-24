
from celery import shared_task

# celery tasks go here ..
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-the-shared-task-decorator

@shared_task
def add(x, y):
    return x + y