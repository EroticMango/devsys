#-*- coding:utf8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig, apps

from django.db.models.signals import post_migrate

def my_callback(sender, **kwargs):
    #=============创建超级用户======================
    from django.contrib.auth.models import User
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

permission_chioces = {
    'logentry': u'日志',
    'permission': u'权限',
    'group': u'用户组',
    'user': u'用户',
    'contenttype': u'权限相关',
    'session': u'登录session',
}

def create_model_permission(model):
    from django.contrib.contenttypes.models import ContentType
    from django.contrib.auth.models import Permission
    ct = ContentType.objects.get_for_model(model)

    '''
        修改默认权限显示名字
            新增
            修改
            删除
    '''
    new_name = model_name = model._meta.model_name
    if model_name in  permission_chioces:
        new_name = permission_chioces[model_name]
    else:
        if hasattr(model._meta, 'verbose_name'):
            new_name = model._meta.verbose_name
    #==============新增权限名字修改===================
    p_add_name = '新增{name}'.format(name=new_name)
    p_add_codename = 'add_{model_name}'.format(model_name=model_name)
    permission = Permission.objects.filter(
        codename=p_add_codename,
        content_type=ct,
    ).update(name=p_add_name)

    #==============修改权限名字修改===================
    p_change_name = '修改{name}'.format(name=new_name)
    p_change_codename = 'change_{model_name}'.format(model_name=model_name)
    permission = Permission.objects.filter(
        codename=p_change_codename,
        content_type=ct,
    ).update(name=p_change_name)

    #==============删除权限名字修改===================
    p_delete_name = '删除{name}'.format(name=new_name)
    p_delete_codename = 'delete_{model_name}'.format(model_name=model_name)
    permission = Permission.objects.filter(
        codename=p_delete_codename,
        content_type=ct,
    ).update(name=p_delete_name)


