# -*- coding: utf-8 -*-
# @Time    : 2023-03-28 23:18
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.contrib import admin
from django.urls import path,include
from app01 import views

urlpatterns = [
    path("send/sms/",views.send_msg),
    path("user/register/",views.register,name="register"),
    path("index/", views.index),

]