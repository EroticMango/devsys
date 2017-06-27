#-*- coding:utf8 -*-
'''
    系统权限比较多大于个人权限 系统跟个人权限一一检验 后期更改为migrations文件处理
'''
from django.apps import apps
from django.db.models import Q
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from base.basemodel import get_all_models
from base.operation import Operation


def get_extra_permissions():
    '''
        返回一个权限list

        获取用户自定义权限以及操作权限
        custom_permission = (('name', 'codename'))
    '''
    all_models = get_all_models()
    extra_permissions = Operation.op_permissions()
    for model in all_models:
        if hasattr(model._meta, 'custom_permission'):
            ct = ContentType.objects.get_for_model(model)
            custom_permission_tuple = model._meta.custom_permission
            custom_permission_list = [{
                                        'name': perm[0],
                                        'codename':perm[1],
                                        'content_type':ct}
                                        for perm in custom_permission_tuple]
            extra_permissions.extend(custom_permission_list)
    return extra_permissions


class PermissionChioces(object):
    '''
        对初始化的权限进行中文翻译
    '''

    def __init__(self, *args, **kwargs):
        self.permission_chioces = {
            'logentry': u'日志',
            'permission': u'权限',
            'group': u'用户组',
            'user': u'用户',
            'contenttype': u'权限相关',
            'session': u'登录session',
        }

    def create_extra_permissions(self, *args, **kwargs):
        Permission.objects.create(**kwargs)

    def delete_extra_permissions(self, *args, **kwargs):
        Permission.objects.delete(**kwargs)

    def check_permissions(self, *args, **kwargs):
        extra_permissions_db = Permission.objects.all().exclude(Q(codename__startswith="add")
                                                                | Q(codename__startswith="change")
                                                                | Q(codename__startswith="delete"))
        extra_permissions = get_extra_permissions()
        self.compare_create_permissions(extra_permissions, extra_permissions_db)

    def compare_create_permissions(self, extra_permissions, extra_permissions_db):
        '''
            比较extra_permissions里面的数据是否在extra_permissions_db中
        '''
        for perm in extra_permissions:
            if not extra_permissions_db.filter(**perm).exists():
                self.create_extra_permissions(**perm)



    def compare_delete_permissions(self, extra_permissions, extra_permissions_db):
        '''
            比较extra_permissions里面的数据是否在extra_permissions_db中
        '''
        pass


    def __getitem__(self, key):
        return self.permission_chioces[key]

    def __setitem__(self, key, value):
        self.permission_chioces[key] = value


permission_chioces = PermissionChioces()
