# 在这里自定义模板标签
from django import template
from rusSta.models import Category,Sidebar,Post

register = template.Library()

@register.simple_tag
def get_category_list():
    # 全站的分类
    return Category.objects.all()

@register.simple_tag
def get_sidebar_list():
    # 全站的分类
    return Sidebar.get_sidebar()

@register.simple_tag
def get_new_post():
    return Post.objects.order_by('-pub_date')[:6]

@register.simple_tag
def get_hot_pv_post():
    return Post.objects.order_by('-pv')[:6]

