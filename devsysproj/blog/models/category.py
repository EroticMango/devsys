#-*- coding:utf8 -*-

from django.db import models
from base.basemodel import BaseCacheModel

class Category(BaseCacheModel):

    category_name = models.CharField(max_length=20, default=u'默认')

    class Meta:
        app_label = 'blog'
