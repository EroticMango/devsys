#-*- coding:utf8 -*-

from django.db import models
from base.basemodel import BaseCacheModel
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase


class Category(BaseCacheModel):

    category_name = models.CharField(max_length=20, default=u'默认')

    class Meta:
        app_label = 'blog'
        verbose_name = u'文章分类'
