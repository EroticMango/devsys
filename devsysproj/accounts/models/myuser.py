#-*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.basemodel import BaseCacheModel
from base.operation import Operation

class MyUser(BaseCacheModel):

    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=128, default='')
    headimg = models.URLField(
        default='http://eroticmango-1253870897.cosgz.myqcloud.com/accounts/img/default.png')

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance=None, created=False, **kwargs):
        # print instance.
        if created and not instance.is_superuser and instance.username != 'AnonymousUser':
            MyUser.objects.get_or_create(user=instance, defaults={'nickname':instance.username})

    class Meta:
        app_label = 'accounts'
        verbose_name = u'扩展用户'


    def reset_secret_url(self):
        '''
            参考bilibili的重置密码
            dopost=getpasswd&id=34438111&key=302faeac863675ff
            执行操作  用户id  key随机生成用来校验（保存4小时，只有一次性）
        '''
        return 'www.baidu.com'
# from django.contrib.auth.models import Group
    class test(Operation):
        pass
