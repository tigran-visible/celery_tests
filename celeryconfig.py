from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

app.conf.update(
    result_expires=3600,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    broker_transport_options={'visibility_timeout': 10}

)
print(app.conf)