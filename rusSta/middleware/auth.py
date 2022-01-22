"""中间件"""
from django.utils.deprecation import MiddlewareMixin
from rusSta import models


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """如果用户已经登录，则在request中赋值"""
        user_id = request.session.get('user_id', 0)  # 如果没有user_id则替换成0
        user_object = models.UserInfo.objects.filter(id=user_id).first()

        request.tracer = user_object
