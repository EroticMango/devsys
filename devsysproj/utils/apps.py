#-*- coding:utf8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig, apps
from django.db.models.signals import post_migrate


def my_callback(sender, **kwargs):
    #=============创建超级用户======================
    from django.contrib.auth.models import User
    from .management import create_model_permission
    admin = User.objects.filter(username='admin')
    if admin.count() < 1:
        user = User.objects.create_superuser('admin', 'admin@qq.com', 'admin')

    all_model = apps.get_models()
    for curmodel in all_model:
        create_model_permission(curmodel)


class UtilsConfig(AppConfig):
    name = 'utils'

    def ready(self):
        post_migrate.connect(my_callback, sender=self)


