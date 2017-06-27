#-*- coding:utf8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.cache import cache
from django.db.models.query import QuerySet
from django.db.models.manager import BaseManager
# from django.core.cache.backends.memcached import MemcachedCache
from cache.memcached import Memcached
from django.core.cache import cache

from django.apps import apps

def get_all_models():
    custom_apps = settings.CUSTOM_APPS
    all_app_models = [apps.get_app_config(app).models for app in custom_apps]
    all_valid_models = []
    for app_models in all_app_models:
        for k, v in app_models.iteritems():
            all_valid_models.append(v)
    return all_valid_models


class QuerySetEx(QuerySet):

    def __init__(self, *args, **kwargs):
        super(QuerySetEx, self).__init__(*args, **kwargs)

    def update(self, **kwargs):
        super(QuerySetEx, self).update(**kwargs)
        for obj in self:
            obj.set_cache_db_key()


# used to cache querset or get cache data
class NewBaseManager(BaseManager.from_queryset(QuerySetEx)):

    def get(self, *args, **kwargs):
        data = None
        selfmodel = self.model
        # print selfmodel
        memcache_obj = selfmodel.memcached()
        query_key = memcache_obj.cache_query_key(**kwargs)
        # print querykey,"querycache===="
        if query_key:
            data_key = memcache_obj.get(query_key)
            if data_key:
                data = memcache_obj.get(data_key)
                if not data:
                    data = super(NewBaseManager, self).get(*args, **kwargs)
                    data.set_cache_db_key()
            else:
                data = super(NewBaseManager, self).get(*args, **kwargs)
                data_key = data.set_cache_db_key()
                memcache_obj.set(query_key, data_key, 60 * 3)
        else:
            data = super(NewBaseManager, self).get(*args, **kwargs)
        return data

    def get_queryset(self):

        return super(NewBaseManager, self).get_queryset()

# get Model type
BaseModel = type(models.Model)

# metacaching create new function


class MetaCaching(BaseModel):

    def __new__(cls, *args, **kwargs):
        # print args, kwargs
        new_class = BaseModel.__new__(cls, *args, **kwargs)
        new_manager = NewBaseManager()
        new_manager.contribute_to_class(new_class, 'objects')
        new_class._meta._default_manager = new_manager
        return new_class

# basecacheModel use for cache


class BaseCacheModel(models.Model):

    create_time = models.DateTimeField(
        verbose_name=u'创建时间', auto_now_add=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        super(BaseCacheModel, self).save(*args, **kwargs)
        self.refresh_from_db()
        self.set_cache_db_key()

    def delete(self, *args, **kwargs):
        super(BaseCacheModel, self).delete(*args, **kwargs)
        self.del_cache_db_key()

    @classmethod
    def memcached(cls, *args, **kwargs):
        return Memcached(cls)

    def cache_db_key(self):
        data_key = '_C_{table_name}_{pk}'.format(
            table_name=self._meta.db_table,
            pk=self.pk)
        return data_key

    def set_cache_db_key(self):
        data_key = self.cache_db_key()
        cache.set(data_key, self, 60 * 15)
        return data_key

    def del_cache_db_key(self):
        data_key = self.cache_db_key()
        cache.delete(data_key)

    class Meta:
        abstract = True

    __metaclass__ = MetaCaching


__all__ = ['BaseCacheModel', ]
