from django.db import models
from django.contrib.auth.models import User
# from django.utils.functional import cached_property  # 缓存装饰器
from django.template.loader import render_to_string  # 渲染模板


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, db_index=True)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)

    USER_GENDER_TYPE = (
        ('male', '男'),
        ('female', '女'),
    )

    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=6, choices=USER_GENDER_TYPE, default='male')
    address = models.CharField('地址', max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='profile_pic/%Y/%m', default='profile_pic/default.png', max_length=100,
                              verbose_name='用户头像')
    star_post = models.ManyToManyField("Post")

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=32, verbose_name='分类名称')
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name='分类描述')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    category_pic = models.ImageField(verbose_name='分类图片', null=True, upload_to='category_pic/')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """文章标签"""
    name = models.CharField(max_length=10, verbose_name='文章标签')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章"""
    title = models.CharField(max_length=61, verbose_name='文章标题')
    owner = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE, verbose_name='作者')
    pv = models.IntegerField(default=0, verbose_name="浏览量")  # 浏览量
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, verbose_name='文章标签')
    picture = models.ImageField(verbose_name='图片', null=True, upload_to='content_picture/%Y /%m/%d/')
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name='简介/摘要/首句')
    content = models.TextField(verbose_name='文章详情')
    annotation = models.TextField(blank=True, default='', verbose_name='文章注释')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



class Sidebar(models.Model):
    # 侧边栏的模型数据
    STATUS = {
        (1, '隐藏'),
        (2, '展示'),
    }
    DISPLAY_TYPE = (
        (1, '搜索'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
        (5, 'HTML')
    )
    title = models.CharField(max_length=50, verbose_name='模块名称')  # 模块名称
    display_type = models.PositiveIntegerField(default=1, choices=DISPLAY_TYPE,
                                               verbose_name='展示类型')  # 侧边栏 搜索框/最新文章/热门文章/HTML自定义等
    content = models.CharField(max_length=500, blank=True, default='', verbose_name='内容',
                               help_text='如果设置的不是HTML类型，可为空')  # 这个字段是专门用来给HTML类型用的，其他类型可为空
    sort = models.PositiveIntegerField(default=1, verbose_name='排序', help_text='序号越大越靠前')
    status = models.PositiveIntegerField(default=2, choices=STATUS, verbose_name='状态')  # 隐藏 显示状态
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 时间

    class Meta:
        verbose_name = '侧边栏'
        verbose_name_plural = verbose_name
        ordering = ['-sort']

    def __str__(self):
        return self.title

    @classmethod
    def get_sidebar(cls):
        return cls.objects.filter(status=2)  # 查询到所有允许展示的模块

    @property  # 成为一个类属性，调用的时候不需要后边的（）,是只读的，用户没办法修改
    def get_content(self):
        if self.display_type == 1:
            context = {

            }
            return render_to_string('sidebar/search.html', context=context)
        elif self.display_type == 2:
            context = {

            }
            return render_to_string('sidebar/new_post.html', context=context)
        elif self.display_type == 3:
            context = {

            }
            return render_to_string('sidebar/hot_post.html', context=context)
        elif self.display_type == 4:
            context = {

            }
            return render_to_string('sidebar/comment.html', context=context)

        elif self.display_type == 5:  # 自定义侧边栏
            return self.content  # 在侧边栏直接使用这里的html,模板中必须使用safe过滤器去渲染HTML




