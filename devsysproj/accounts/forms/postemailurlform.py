#-*- coding:utf8 -*-

from rest_framework import serializers

from django.contrib.auth.models import User

from accounts.models.myuser import MyUser
from accounts.tasks import send_mail_task

class PostEmailUrlForm(serializers.Serializer):

    email = serializers.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(PostEmailUrlForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, data):

        user_objs = User.objects.filter(email=data['email'])

        if user_objs.count() > 0:
            self.user = user_objs[0]
        else:
            raise serializers.ValidationError(u'该邮箱未注册')

        return data

    def send_email(self):
        myuser_obj = MyUser.objects.get(user=self.user)
        msg = u'密码重置链接{reset_url}'.format(reset_url=myuser_obj.reset_secret_url())
        kw_list = [u'重置密码', msg, u'shellyhh@163.com', [self.user.email,]]
        send_mail_task.delay(list(kw_list))
