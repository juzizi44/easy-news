from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import UserInfo,Category,Tag,Post
from utils import encrypt
from django.contrib.auth.admin import UserAdmin

# # 取消关联注册User
# admin.site.unregister(User)
#
# # 定义关联对象的样式，StackedInline为纵向排列每一行，TabularInline为并排排列
# class UserProfileInline(admin.StackedInline):
#     model = UserInfo # 关联的模型

#
# 关联UserProfile
# class UserProfileAdmin(UserAdmin):
#     inlines = [UserProfileInline]

# 注册User模型

admin.site.register(UserInfo)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)


