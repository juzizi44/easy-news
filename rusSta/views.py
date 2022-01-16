from django.shortcuts import render, HttpResponse

# Create your views here.

import random
from utils.tencent.sms import send_sms_single
from django.conf import settings


def send_sms(request):
    """发送短信"""
    code = random.randrange(1000, 9999)
    res = send_sms_single('3454353', 548760, [code, ])
    print(res)
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])


from django import forms
from rusSta import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    # django里面没有专门针对手机号的验证，在这里可以重写
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput())
    # 重复密码验证
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    # 短信验证码
    code = forms.CharField(label='验证码',widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        fields = ['username','email','password','confirm_password','mobile_phone','code']

    def __init__(self, *args, **kwargs):  # 给每个字段都加上form-control属性
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
