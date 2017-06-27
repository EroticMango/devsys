#-*- coding:utf8 -*-

from django.db import models

from base.basemodel import BaseCacheModel

from accounts.models.myuser import MyUser


class Tag(BaseCacheModel):

    tag_name = models.CharField(max_length=20, default=u'默认')
    author = models.ForeignKey(MyUser)

    class Meta:
        app_label = 'blog'
        verbose_name = u'文章标签'

    class Admin:
        ordinary_permission = ('add_tag',)
        ordinary_obj_permission = ('delete_tag', 'change_tag')
