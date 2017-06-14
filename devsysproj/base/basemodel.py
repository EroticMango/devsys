#-*- coding:utf8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.cache import cache
# from cache.basecache import cachekey

class Cache(object):

    @classmethod
    def cache_db_key(cls, obj):
        return '_C_{table_name}_{pk}'.format(
        table_name=obj._meta.db_table,
        pk=obj.pk)

    @classmethod
    def cache_query_key(cls, model, **kwargs):
        kw_str = ""
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        for k,v in kwargs.items():
            if isinstance(v, models.Model):
                # print v._meta.app_label, v._meta.model_name, v.pk
                if kw_str:
                    kw_str += ":"
                kw_str += "%s:%s" % (k, v.pk)
            else:
                if kw_str:
                    kw_str += ":"
                kw_str += "%s:%s" % (k, v)
        return "%s_%s_%s" % (app_label, model_name, kw_str)


# used to cache querset or get cache data
class NewBaseManager(models.Manager):

    def get(self, *args, **kwargs):
        # data = None
        # selfmodel = self.model
        # querykey = cachekey.cache_key(model=selfmodel, **kwargs)
        # datakey = cache.get(querykey)
        # if datakey:
        #     data = cache.get(datakey)
        #     if data:
        #         return data
        print "3333333"
        data = super(NewBaseManager, self).get(*args, **kwargs)
        # if data:
        #     datakey = cachekey.make_key(data)
        #     cache.set(querykey, datakey, 60*3)
        #     cache.set(datakey, data, 60*15)
        return data

    def get_queryset(self):

        return super(NewBaseManager, self).get_queryset()
# get Model type
BaseModel = type(models.Model)

# metacaching create new function
class MetaCaching(BaseModel):

    def __new__(cls, *args, **kwargs):
        new_class = BaseModel.__new__(cls, *args, **kwargs)
        new_manager = NewBaseManager()
        new_manager.contribute_to_class(new_class, "objects")
        new_class._meta._default_manager = new_manager
        return new_class

#basecacheModel use for cache
class BaseCacheModel(models.Model):

    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        super(BaseCacheModel, self).save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        super(BaseCacheModel, self).delete(*args, **kwargs)

    class Meta:
       abstract = True

    __metaclass__ = MetaCaching


__all__ = ['BaseCacheModel',]
