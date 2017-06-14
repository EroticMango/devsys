#-*- coding:utf8 -*-

from celery.task import task

from base.emailbase import post_mail_to_user

@task
def send_mail_task(datatuple):
    try:
        post_mail_to_user(datatuple)
    except:
        import traceback;traceback.print_exc()
