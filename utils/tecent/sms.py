# -*- coding: utf-8 -*-
# @Time    : 2023-03-22 15:19
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : sms.py
# @Software: PyCharm
import ssl
# ssl._create
#导入配置文件
# from django.conf import settings
from Sass_Django import settings
from qcloudsms_py import SmsMultiSender,SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
def send_sms_single(phone_num,template_id,template_param_list):
    '''

    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    '''
    # appid=112142311 #应用id
    # appkey="8cc5b87123y4234234123879300004"#应用key
    # sms_sign="python之路" #腾讯云创建签名时填写的签名内容.
    appid=settings.TENCENT_SMS_APP_ID
    appkey=settings.TENCENT_SMS_APP_KEY
    sms_sign=settings.TENCENT_SMS_SIGN
    sender=SmsSingleSender(appid,appkey)
    try:
        response=sender.send_with_param(86,phone_num,template_id,template_param_list,sign=sms_sign)
    except HTTPError as e:
        response={'result':100,'errmsg':"网络异常发送失败"}
    except TypeError as  e:
        response={'result':100,'errmsg':"格式错误"}

    return response

def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量发送短信
    :param phone_num_list:手机号列表
    :param template_id:腾讯云短信模板ID
    :param param_list:短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid=settings.TENCENT_SMS_APP_ID
    appkey=settings.TENCENT_SMS_APP_KEY
    sms_sign=settings.TENCENT_SMS_SIGN
    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response

if  __name__=="__main__":
    result1=send_sms_single("18171799952",548760,[666,])
    print(result1)
    result2=send_sms_single({"18171799952","18171799952","18171799952",},548760,[999,])
    print(result2)
