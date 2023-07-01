# 一个基于Django+Mysql的资讯平台

## 安装方法

- 新建并且激活环境

```bash
python -m venv venv 
.\venv\Scripts\Activate.ps1  
```

- 下载依赖

```bash
pip install -r requirement.txt
```

- 修改数据库配置文件

（在此之前需要在mysql中新建一个database）

`djangoProject1\settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'russta',#修改成自己的数据库名称
        'USER': 'root',
        'PASSWORD': 'yourpassword',#修改成自己的密码
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```

- 数据库迁移

```bash
python manage.py makemigrations  
python manage.py migrate
```

- 运行

```
python manage.py runserver
```

## 简介

- 功能架构

![内容架构](./assets/clip_image002.jpg)

- 登录注册地址：http://127.0.0.1:8000/

![image-20230701232817452](./assets/image-20230701232817452.png)

![image-20220227124702310](./assets/image-20220227124702310.png)

- 官网地址：http://127.0.0.1:8000/web/

![image-20230701233014771](./assets/image-20230701233014771.png)

- 后台地址：http://127.0.0.1:8000/admin/

![image-20220225000556514-164593838601018](./assets/image-20220225000556514-164593838601018.png)

