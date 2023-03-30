# -*- coding: utf-8 -*-
# @Time    : 2023-03-26 20:54
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : account.py
# @Software: PyCharm
from django.shortcuts import  render
"""
用户账户相关功能：注册、短信、登录、注册
"""
def register(request):
    return render(request, "web/register.html")