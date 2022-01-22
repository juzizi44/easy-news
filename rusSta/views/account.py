from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect
from rusSta.forms.account import RegisterModelForm, LoginForm
from django.http import JsonResponse
from rusSta import models


from django.db.models import Q
from utils.image_code import check_code


def register(request):
    """注册"""
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, '../templates/register.html', {'form': form})
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过，写入数据库(密码要是密文)
        form.save()
        return JsonResponse({'status': True, 'data': '/login/'})
    return JsonResponse({'status': False, 'error': form.errors})


def login(request):
    """用户名和密码登录"""
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, '../templates/login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        #  验证通过，跳转

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        code = form.cleaned_data['code']

        user_object = models.UserInfo.objects.filter(
            Q(email=username) | Q(mobile_phone=username) | Q(username=username)).filter(
            password=password).first()
        if user_object:
            # 用户名密码正确,登录成功
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 14)  # 用户登陆成功之后用户信息保存两周
            return redirect('index')

        form.add_error('username', '用户名或密码错误')

    return render(request, '../templates/login.html', {'form': form})


def image_code(request):
    """生成图片验证码"""
    from utils.image_code import check_code
    from io import BytesIO
    image_object, code = check_code()
    request.session['image_code'] = code  # 把字符串存到服务器的这个人的session里面
    request.session.set_expiry(60)  # 主动修改session的过期时间是60s，设置验证码的超时时间
    stream = BytesIO()
    image_object.save(stream, 'png')

    return HttpResponse(stream.getvalue())

def logout(request):
    #  点击退出，清除session里面的id
    request.session.flush()
    return redirect('index')