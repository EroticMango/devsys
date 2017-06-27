#-*- coding:utf8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig, apps
from django.db.models.signals import post_migrate


def my_callback(sender, **kwargs):
    #=============创建超级用户======================
    from django.contrib.auth.models import User, Group
    from base.management import create_model_permission, create_ordinary_group_permissions
    admin = User.objects.filter(username='admin')
    if admin.count() < 1:
        user = User.objects.create_superuser('admin', 'admin@qq.com', 'admin')
    #=============修改权限名称=====================
    all_model = apps.get_models()
    for curmodel in all_model:
        create_model_permission(curmodel)

    #=============初始化普通用户基本权限组====================
    ordinary_group = Group.objects.get_or_create(name=u'普通会员')[0]
    create_ordinary_group_permissions(ordinary_group)




class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        post_migrate.connect(my_callback)

