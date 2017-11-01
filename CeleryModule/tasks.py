from celery import Celery

app = Celery('CeleryModule', broker='amqp://localhost')

@app.task
def add(x, y):
    return x + y