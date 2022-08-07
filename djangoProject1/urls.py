"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rusSta.views import account, home
from utils.upload import upload_file


urlpatterns = [
    path('', home.index, name='index'),
    path('admin/', admin.site.urls),
    path('web/', home.web, name='web'),
    path('register/', account.register, name='register'),
    path('login/', account.login_view, name='login'),
    path('image/code/', account.image_code, name='image_code'),
    path('index/', home.index, name='index'),
    path('logout/', account.logout, name='logout'),
    path('category/<int:category_id>/', home.category_list, name='category_list'),
    path('post/<int:category_id>/<int:post_id>/', home.post_detail, name='post_detail'),
    path('post/<int:category_id>/<int:post_id>/star', home.star, name='post_star'),
    path('post/<int:category_id>/<int:post_id>/unstar', home.unstar, name='post_unstar'),

    path('search/', home.search, name='search'),
    path('uploads/', upload_file, name='uploads'),  # 上传图片url
    # path('user_profile/<str:user_name>/', home.user_profile, name='user_profile'),
    path('user_conllection/', home.user_collection, name='user_collection'),
    path('user_post/', home.user_post, name='user_post')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
