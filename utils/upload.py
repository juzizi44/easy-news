"""后台富文本编辑器中的图片上传"""
import os
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings


@csrf_exempt
def upload_file(request):
    """ ckeditor5图片上传 """
    upload = request.FILES.get('upload')
    # 生成uuid 
    uid = ''.join(str(uuid.uuid4()).split('-'))
    # 修改图片名称 
    names = str(upload.name).split('.')
    names[0] = uid
    # 拼接图片名
    upload.name = '.'.join(names)
    # 构造上传路径
    new_path = os.path.join(settings.MEDIA_ROOT, 'upload/', upload.name)
    # 上传图片
    with open(new_path, 'wb+') as destination:
        for chunk in upload.chunks():
            destination.write(chunk)

    # 构造要求的数据格式并返回
    filename = upload.name
    url = '/media/upload/' + filename
    retdata = {'url': url,
               'uploaded': '1',
               'fileName': filename}
    return JsonResponse(retdata)
