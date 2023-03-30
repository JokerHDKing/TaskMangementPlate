# -*- coding: utf-8 -*-
# @Time    : 2023-03-28 23:18
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.contrib import admin
from django.urls import path,include
from  web.views import account
urlpatterns = [
    path('register/$',account.register,name='register')

]