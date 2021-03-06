#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

"""
@version: python3.5.2
@author: King Suo 
@contact: 2354917594@qq.com
@software: PyCharm
@file: urls.py
@time: 2018/2/28 下午2:01
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.schemas import get_schema_view

from snippets.views import SnippetViewSet, UserViewSet, api_root

schema_view = get_schema_view(title='Pastebin API')

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^schema/$', schema_view),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])