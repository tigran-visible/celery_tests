from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y

@app.task(acks_late=True, reject_on_worker_lost=True)
def long_task():
    import time
    time.sleep(60)
    return "Task completed"
