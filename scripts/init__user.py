"""离线脚本"""
import os
import sys
import django
from utils import encrypt
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'djangoProject1.settings')
django.setup()  # os.environ['DJANGO_SETTINGS_MODULE']

from rusSta import models
# 往数据库添加数据：链接数据库、操作、关闭连接
models.UserInfo.objects.create(username='陈硕',email='chengshuo@163.com',
                               mobile_phone='13838383838',password=encrypt.md5('123123'))

