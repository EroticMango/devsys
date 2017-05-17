#-*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUser(models.Model):

    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=128, default='')

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance=None, created=False, **kwargs):
        # print instance.
        if created and not instance.is_superuser and instance.username != 'AnonymousUser':
            MyUser.objects.get_or_create(user=instance, defaults={'nickname':instance.username})

    class Meta:
        app_label = 'accounts'
        verbose_name = u'扩展用户'


# from django.contrib.auth.models import Group
