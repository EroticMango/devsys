#-*- coding:utf8 -*-

from django.core.mail import send_mass_mail

import smtplib

def post_mail_to_user(*args):
    datatuple = args[0]
    try:
        send_mass_mail((datatuple, ), fail_silently=False)
    except smtplib.SMTPException as e:
        print e

