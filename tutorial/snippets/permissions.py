#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

"""
@version: python3.5.2
@author: King Suo 
@contact: 2354917594@qq.com
@software: PyCharm
@file: permissions.py.py
@time: 2018/2/28 下午4:53
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
