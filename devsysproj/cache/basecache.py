#-*- coding:utf8 -*-

from threading import local

from django.db import models


class BaseCache(local):

    def __init__(self, model):
        self.model = model

    def cache_query_key(self, **kwargs):
        kw_str_list = []
        app_label = self.model._meta.app_label
        model_name = self.model._meta.model_name
        for k, v in kwargs.items():
            if isinstance(v, models.Model):
                # print v._meta.app_label, v._meta.model_name, v.pk
                kw_str_list.append(':'.join([k, str(v.pk)]))
            else:
                kw_str_list.append(':'.join([k, str(v)]))
        kw_str = ':'.join(kw_str_list)
        return '_'.join([app_label, model_name, kw_str])

    def set(self, key, value, timeout, version=None):
        raise NotImplementedError

    def delete(self, key, version=None):
        raise NotImplementedError

    def get(self, key, version=None):
        raise NotImplementedError
