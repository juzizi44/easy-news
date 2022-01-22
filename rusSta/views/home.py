from django.shortcuts import render, get_object_or_404
from rusSta import models
from rusSta.models import Category, Post


def index(request):
    # 查询首页数据并显示在页面
    category_list = models.Category.objects.all()  # 查询到所有的分类
    post_list = models.Post.objects.all()  # 查询到所有的文章
    context = {'category_list': category_list, 'post_list': post_list}
    return render(request, 'index.html', context)


def category_list(request, category_id):
    # 查询首页数据并显示在页面
    category_list = models.Category.objects.all()  # 查询到所有的分类
    category = get_object_or_404(Category, id=category_id)
    posts = category.post_set.all()
    context = {'category': category, 'category_list': category_list,'posts':posts}

    return render(request, 'list.html', context)
