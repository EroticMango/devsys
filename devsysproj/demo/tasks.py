from celery.task import task
from celery.signals import task_success

@task
def add(x, y):
    from time import sleep
    sleep(10)
    return x + y


@task
def sleeptask(i):
    from time import sleep
    sleep(i)
    return i


@task
def raisetask():
    raise KeyError("foo")


@task_success.connect
def task_send_hander(sender=None, result=None, **kwargs):
    task_id = sender.request.id
    print task_id
