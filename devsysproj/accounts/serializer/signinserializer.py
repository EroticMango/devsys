#-*- coding:utf8 -*-

from rest_framework import serializers

from accounts.models.myuser import MyUser

class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('nickname', 'headimg')
