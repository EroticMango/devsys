#-*- coding:utf8 -*-

from rest_framework import serializers

import re

from django.contrib.auth.models import User

class SignInForm(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
