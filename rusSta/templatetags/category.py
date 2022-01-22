# 在这里自定义模板标签
from django import template
from rusSta.models import Category

register = template.Library()

@register.simple_tag
def get_category_list():
    return Category.objects.all()
