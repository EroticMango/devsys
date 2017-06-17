#-*- coding:utf8 -*-

from .basecache import BaseCache

from django.core.cache import cache


class Memcached(BaseCache):

    def __init__(self, model):
        super(Memcached, self).__init__(model)


    def set(self, key, value, timeout, version=None):
        try:
            cache.set(key, value, timeout)
        except Exception as e:
            import traceback;traceback.print_exc()

    def delete(self, key, version=None):
        cache.delete(key)

    def get(self, key, version=None):
        return cache.get(key)



