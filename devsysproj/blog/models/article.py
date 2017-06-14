#-*- coding:utf8 -*-

from base.basemodel import BaseCacheModel

from django.db import models

'''
    作者
    内容
    标题
    分类
    标签
    评论
    匿名聊天
'''

class Article(BaseCacheModel):
    article_title = models.CharField(max_length=30, default='')
    content = models.TextField(default='')
    author =

    class Meta:
        app_label= 'blog'
