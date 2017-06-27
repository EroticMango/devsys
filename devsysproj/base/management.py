#-*- coding:utf8 -*-

from base.permission import permission_chioces
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


def create_model_permission(model):

    ct = ContentType.objects.get_for_model(model)

    '''
        修改默认权限显示名字
            新增
            修改
            删除
    '''
    model_name = model._meta.model_name
    new_name = permission_chioces[
        model_name] or model._meta.verbose_name or model_name
    #==============新增权限名字修改===================
    p_add_name = u'新增{name}'.format(name=new_name)
    p_add_codename = 'add_{model_name}'.format(model_name=model_name)
    permission = Permission.objects.filter(
        codename=p_add_codename,
        content_type=ct,
    ).update(name=p_add_name)

    #==============修改权限名字修改===================
    p_change_name = u'修改{name}'.format(name=new_name)
    p_change_codename = 'change_{model_name}'.format(model_name=model_name)
    permission = Permission.objects.filter(
        codename=p_change_codename,
        content_type=ct,
    ).update(name=p_change_name)

    #==============删除权限名字修改===================
    p_delete_name = u'删除{name}'.format(name=new_name)
    p_delete_codename = 'delete_{model_name}'.format(model_name=model_name)
    permission = Permission.objects.filter(
        codename=p_delete_codename,
        content_type=ct,
    ).update(name=p_delete_name)


def create_ordinary_group_permissions(group):
    try:
        permission_chioces.create_ordinary_group_permission(group)
    except:
        import traceback
        traceback.print_exc()
