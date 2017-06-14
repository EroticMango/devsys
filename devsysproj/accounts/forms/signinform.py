#-*- coding:utf8 -*-

from rest_framework import serializers

class SignInForm(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

