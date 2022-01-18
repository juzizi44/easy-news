from django.shortcuts import render, HttpResponse
from rusSta.forms.account import RegisterModelForm, LoginForm
from django.http import JsonResponse


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
    form = LoginForm()
    return render(request, '../templates/login.html', {'form': form})
    pass


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
