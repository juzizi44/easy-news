"""
用户账户相关的功能：注册、登录、注销
"""
from django import forms
from rusSta import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from utils import encrypt
from rusSta.forms.bootstrap import BootStrapForm
from rusSta.views import account


class RegisterModelForm(BootStrapForm, forms.ModelForm):
    # django里面没有专门针对手机号的验证，在这里可以重写
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])

    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=30,
        error_messages={
            'min_length': "密码长度不能小于8个字符",
            'max_length': "密码长度不能大于30个字符"
        },
        widget=forms.PasswordInput()
    )
    # 重复密码验证
    confirm_password = forms.CharField(
        label='重复密码',
        min_length=8,
        max_length=30,
        error_messages={
            'min_length': "重复密码长度不能小于8个字符",
            'max_length': "重复密码长度不能大于30个字符"
        },
        widget=forms.PasswordInput())

    class Meta:
        model = models.UserInfo
        fields = ['username', 'email', 'mobile_phone', 'password', 'confirm_password']

    def clean_username(self):
        username = self.cleaned_data['username']
        exists = models.UserInfo.objects.filter(username=username).exists()
        if exists:
            raise ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        exists = models.UserInfo.objects.filter(email=email).exists()  # 可能有问题
        if exists:
            raise ValidationError('邮箱已存在')
        return email

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('手机号已注册')
        return mobile_phone

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密并返回
        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data['password']
        confirm_pwd = encrypt.md5(self.cleaned_data['confirm_password'])
        if pwd != confirm_pwd:
            raise ValidationError('两次密码不一致')
        return confirm_pwd


class LoginForm(BootStrapForm, forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput(render_value=True))
    code = forms.CharField(label='图片验证码')

    class Meta:
        fields = ['username', 'password', 'code']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    #
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     return username

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密并返回
        return encrypt.md5(pwd)

    def clean_code(self):
        """图片验证码是否正确"""
        # 读取用户输入的验证码
        code = self.cleaned_data['code']
        # 去session获取自己的验证码

        session_code = self.request.session.get('image_code')
        # if not session_code:
        #     raise ValidationError('验证码已过期，请重新获取')
        if code.strip().upper() != session_code.strip().upper():
            raise ValidationError('验证码输入错误')

        return code
