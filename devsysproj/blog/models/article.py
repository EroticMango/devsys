#-*- coding:utf8 -*-

from base.basemodel import BaseCacheModel

from django.db import models

from accounts.models.myuser import MyUser

from blog.models.category import Category
from blog.models.tag import Tag


class Article(BaseCacheModel):
    '''
        作者
        内容
        标题
        分类
        标签
        评论
        匿名聊天
    '''
    article_title = models.CharField(max_length=30, default='')
    content = models.TextField(default='')
    author = models.ForeignKey(MyUser)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'blog'
        verbose_name = u'文章'


    class Admin:
        ordinary_permission = ('add_article',)
        ordinary_obj_permission = ('delete_article', 'change_article')
