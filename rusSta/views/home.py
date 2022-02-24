from django.shortcuts import render, get_object_or_404, redirect
from rusSta import models
from rusSta.models import Category, Post, UserInfo
from django.db.models import Q, F
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def web(request):
    return render(request, 'web.html',)

def index(request):
    # 查询首页数据并显示在页面
    category_list = models.Category.objects.all()  # 查询到所有的分类
    posts = Post.objects.order_by('-pub_date')[:3]
    my_collect = models.UserInfo.objects.filter(username=request.tracer).first().star_post.all().order_by('-pub_date')[:3]
    my_post = models.Post.objects.filter(owner=request.tracer).all().order_by('-pub_date')[:3]
    context = {'category_list': category_list,'posts':posts,'my_collect':my_collect,'my_post':my_post}
    return render(request, 'index.html', context)


def category_list(request, category_id):

    category_list = models.Category.objects.all()  # 查询到所有的分类
    category = get_object_or_404(Category, id=category_id)
    posts = category.post_set.all()
    # 分页办法
    paginator = Paginator(posts, 4)  # 第二个参数2代表每页显示几个
    page_number = request.GET.get('page')  # http://assas.co/?page=1(页码）
    page_obj = paginator.get_page(page_number)

    context = {'category': category, 'category_list': category_list, 'posts': posts, 'page_obj': page_obj}

    return render(request, 'list.html', context)


def post_detail(request, category_id, post_id):
    # 文章详情页
    category_list = models.Category.objects.all()  # 查询到所有的分类
    post = get_object_or_404(Post, id=post_id)
    category = get_object_or_404(Category, id=category_id)
    prev_post = models.Post.objects.filter(id__lt=post_id, category_id=category_id).last()  # 上一篇的queryset数据
    next_post = models.Post.objects.filter(id__gt=post_id, category_id=category_id).first()  # 下一篇的queryset数据
    flag = post in models.UserInfo.objects.filter(username=request.tracer).first().star_post.all()

    context = {'category_list': category_list, 'category': category, 'post': post, 'prev_post': prev_post,
               'next_post': next_post, 'flag': flag}
    models.Post.objects.filter(id=post_id).update(pv=F('pv') + 1)
    return render(request, 'detail.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    category_list = models.Category.objects.all()  # 查询到所有的分类

    # 没有搜索默认显示所有文章
    if not keyword:
        post_list = models.Post.objects.all()
    else:
        post_list = models.Post.objects.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(desc__icontains=keyword))

        # 分页办法
    paginator = Paginator(post_list, 6)  # 第二个参数2代表每页显示几个
    page_number = request.GET.get('page')  # http://assas.co/?page=1(页码）
    page_obj = paginator.get_page(page_number)
    context = {
        'category_list': category_list,
        # 'post_list': post_list
        'page_obj': page_obj
    }

    return render(request, 'search_list.html', context)


def user_profile(request, user_name):
    category_list = models.Category.objects.all()  # 查询到所有的分类
    user = get_object_or_404(UserInfo, username=user_name)
    context = {'user': user, 'category_list': category_list}
    return render(request, 'user_profile.html', context)


def user_collection(request):
    my_collect = models.UserInfo.objects.filter(username=request.tracer).first().star_post.all()

    category_list = models.Category.objects.all()  # 查询到所有的分类

    context = {'category_list': category_list, 'my_collect': my_collect}
    return render(request, 'user_collection.html', context)

def user_post(request):
    my_post = models.Post.objects.filter(owner=request.tracer).all().order_by('-pub_date')[:3]

    category_list = models.Category.objects.all()  # 查询到所有的分类

    context = {'category_list': category_list, 'my_post': my_post}
    return render(request, 'user_post.html', context)

def star(request, category_id, post_id):
    post = get_object_or_404(Post, id=post_id)
    person = models.UserInfo.objects.filter(username=request.tracer).first()
    person.star_post.add(post)
    return redirect('post_detail', category_id, post_id)


def unstar(request, category_id, post_id):
    person = models.UserInfo.objects.filter(username=request.tracer).first()
    d = person.star_post.filter(id=post_id)
    person.star_post.remove(*d)

    return redirect('post_detail', category_id, post_id)
