#-*- coding:utf8 -*-

from django.db import models

from base.basemodel import BaseCacheModel

from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase

from accounts.models.myuser import MyUser


class Category(BaseCacheModel):

    category_name = models.CharField(max_length=20, default=u'默认')
    author = models.ForeignKey(MyUser)

    class Meta:
        app_label = 'blog'
        verbose_name = u'文章分类'

    class Admin:
        ordinary_permission = ('add_category',)
        ordinary_obj_permission = ('delete_category', 'change_category')
