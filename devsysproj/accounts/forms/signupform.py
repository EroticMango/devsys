#-*- coding:utf8 -*-

from rest_framework import serializers

import re

from django.contrib.auth.models import User

class SignUpForm(serializers.Serializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=16, min_length=6)


    def validate(self, data):

        not_chinese_rule = re.compile(u'[\u4e00-\u9fa5]+')
        is_chinese = not_chinese_rule.findall(data['username'])
        if is_chinese:
            raise serializers.ValidationError(u'不允许包含中文')

        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
