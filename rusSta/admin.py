from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import UserInfo, Category, Tag, Post, Sidebar

from django.contrib import admin

admin.site.site_header = '俄语小站管理后台'  # 设置header
admin.site.site_title = '俄语小站管理后台'  # 设置title
admin.site.index_title = '俄语小站管理后台'


admin.site.register(UserInfo)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Sidebar)



class PostAdmin(admin.ModelAdmin):
    """文章详情管理"""
    list_display = ('id', 'title', 'category', 'tags', 'owner', 'pv', 'pub_date',)
    list_filter = ('owner',)
    search_fields = ('title', 'desc')
    list_display_links = ('title',)

    class Media:
        css = {
            "all": ('plugin/ckeditor5/cked.css',)
        }
        js = (
            'https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js',
            'plugin/ckeditor5/ckeditor.js',
            'plugin/ckeditor5/translations/zh.js',
            'plugin/ckeditor5/config.js',
        )


admin.site.register(Post, PostAdmin)
