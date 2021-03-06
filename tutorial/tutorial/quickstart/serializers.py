#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

"""
@version: python3.5.2
@author: King Suo 
@contact: 2354917594@qq.com
@software: PyCharm
@file: serializers.py.py
@time: 2018/2/27 下午1:56
"""

from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

