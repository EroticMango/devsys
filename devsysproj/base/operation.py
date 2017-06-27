#-*- coding:utf8 -*-
'''
       op_name
'''

from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

import types

from base.basemodel import get_all_models

class Operation(object):

    def op_log(self):
        print "操作日志"

    @classmethod
    def op_permissions(cls, *args, **kwargs):
        """
            Return op permission list
            By default return a empty list
        """
        all_models = get_all_models()
        all_permissions = []
        for model in all_models:
            for attr_name in dir(model):
                attr = getattr(model, attr_name)
                if isinstance(attr, types.TypeType) and issubclass(attr, cls):
                    try:
                        ct = ContentType.objects.get_for_model(model)
                    except:
                        ct =None
                    op_permission_dict = {
                        'name': attr.verbose_name or attr.__name__,
                        'codename':'_'.join([attr.__name__,model.__name__.lower]),
                        'content_type': ct or '',
                    }
                    all_permissions.append(op_permission_dict)
        return all_permissions
