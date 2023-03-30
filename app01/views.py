from django.shortcuts import render,HttpResponse
from utils.tecent.sms import send_sms_single
import random
from django.conf import settings
from  django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django_redis import get_redis_connection


# Create your views here.
def send_msg(request):
    """发送短信
        ?type=login -->5486724
        ?tpl=register -->548760
        # 没钱用不了捏
    """
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    print(template_id)
    code=random.randrange(1000,9999)
    res=send_sms_single('18171799952',template_id,[code,])
    print(res)
    if res['result']==0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])

from  django import forms
from app01 import models

#modelForm 可以重写字段
class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    password=forms.CharField(label="密码",widget=forms.PasswordInput())
    confirm_password=forms.CharField(label="重复密码",widget=forms.PasswordInput())
    #验证码
    code=forms.CharField(label="验证码",widget=forms.TextInput())
    class Meta:
        model=models.UserInfo
        # fields="__all__"
        #自定义展示顺序
        fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']='请输入%s' %(field.label)


def register(request):
    """注册"""
    form=RegisterModelForm ()
    return render(request,"app01/register.html",{'form':form})

def index(request):
    #去连接池获取一个连接
    conn=get_redis_connection("default")
    conn.set('name','小',ex=10)
    value=conn.get('name')
    print(value)
    return HttpResponse("ok")