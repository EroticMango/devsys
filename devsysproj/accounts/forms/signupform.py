#-*- coding:utf8 -*-

from rest_framework import serializers

import re

from django.contrib.auth.models import User, Group
from django.db.models import Q

from rest_framework.response import Response

from base.response import handle_response_data, form_error

class SignUpForm(serializers.Serializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=16, min_length=6)


    def validate(self, data):

        not_chinese_rule = re.compile(u'[\u4e00-\u9fa5]+')
        is_chinese = not_chinese_rule.findall(data['username'])
        if is_chinese:
            raise serializers.ValidationError(u'不允许包含中文')

        user_objs = User.objects.filter(username=data['username'])
        if user_objs.count() > 0:
            raise serializers.ValidationError(u'该用户名已经被注册')

        user_objs = User.objects.filter(email=data['email'])
        if user_objs.count() > 0:
            raise serializers.ValidationError(u'该邮箱已经被注册')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        ordinary_group = Group.objects.get(name=u'普通会员')
        user.groups.add(ordinary_group)
        return user
