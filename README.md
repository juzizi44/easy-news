# 网站总览

## 官网

![image-20220224234510935](README.assets/image-20220224234510935-16459383860081.png)

![image-20220227124522944](README.assets/image-20220227124522944-16459383860092.png)

![image-20220224234620793](README.assets/image-20220224234620793-16459383860093.png)

![image-20220224234644387](README.assets/image-20220224234644387-16459383860094.png)



![image-20220227124829202](README.assets/image-20220227124829202-16459383860105.png)



## 登陆注册

- 注册

![image-20220224212804086](README.assets/image-20220224212804086-16459383860106.png)

- 登录

![image-20220224212736166](README.assets/image-20220224212736166-16459383860107.png)

## 首页

![image-20220227124702310](README.assets/image-20220227124702310-16459383860108.png)

## 分类页

- 新闻资讯

![image-20220227130004284](README.assets/image-20220227130004284.png)

- 名人介绍

![](README.assets/image-20220227125804071.png)

- 俄罗斯名画

![image-20220227125822397](README.assets/image-20220227125822397.png)

- 电影交流

![image-20220227125836402](README.assets/image-20220227125836402.png)

- 俄语角

![image-20220227125929436](README.assets/image-20220227125929436.png)

## 搜索页

![网页捕获_24-2-2022_234041_127.0.0.1](README.assets/网页捕获_24-2-2022_234041_127.0.0.1-16459383860109.jpeg)

## 我的收藏页

![image-20220227124916008](README.assets/image-20220227124916008-164593838601010.png)

## 我的文章页

![image-20220227124939521](README.assets/image-20220227124939521-164593838601011.png)

## 文章详情页

![网页捕获_24-2-2022_234332_127.0.0.1](README.assets/网页捕获_24-2-2022_234332_127.0.0.1-164593838601012.jpeg)



- 

![image-20220227130414768](README.assets/image-20220227130414768.png)

## 管理后台

- 后台用户数据

![image-20220224213040949](README.assets/image-20220224213040949-164593838601013.png)

![image-20220224213107919](README.assets/image-20220224213107919-164593838601014.png)

- 文章分类模型

![image-20220227125040215](README.assets/image-20220227125040215-164593838601015.png)

- 文章标签模型

![image-20220225000514920](README.assets/image-20220225000514920-164593838601016.png)

![image-20220225000534189](README.assets/image-20220225000534189-164593838601017.png)

- 文章模型

![image-20220225000556514](README.assets/image-20220225000556514-164593838601018.png)

![image-20220225000639178](README.assets/image-20220225000639178-164593838601019.png)

![image-20220225000653628](README.assets/image-20220225000653628-164593838601020.png)

- 侧边栏模型

![image-20220225000127759](README.assets/image-20220225000127759-164593838601121.png)

![image-20220225000149717](README.assets/image-20220225000149717-164593838601122.png)



# 虚拟环境搭建

- pip install virtualenv

- 进入 放置虚拟环境的文件夹：
  - cd D:\Envs


- 创建虚拟环境 rusSta

  - python -m virtualenv rusSta

- 激活虚拟环境：

  - cd D:\Envs\russianSta\Scripts
  - activate

- 注意：pycharm2.0版本如果要建立django项目，那么需要调整pip版本，不然无法成功建立

  - python -m pip install pip==20.2.4

  - ![image-20220116112908295](README.assets/image-20220116112908295.png)

  - 然后去pycharm里面新建项目

    ![image-20220119105720742](README.assets/image-20220119105720742.png)



# 注册登录功能逻辑

注：文档中只是宏观展示代码，并不完全。

## 模板层

（代码未截全）

![image-20220224212108335](README.assets/image-20220224212108335.png)

![image-20220224212122444](README.assets/image-20220224212122444.png)

## 视图层

（代码未截全）

![image-20220224212154536](README.assets/image-20220224212154536.png)



## 模型层

![image-20220224212457848](README.assets/image-20220224212457848.png)

## utils

### 加密密码

![image-20220224212540592](README.assets/image-20220224212540592.png)

### 验证码生成

![image-20220224212615988](README.assets/image-20220224212615988.png)

## 效果展示

- 注册页面

![image-20220224212804086](README.assets/image-20220224212804086.png)

- 登录页面

![image-20220224212736166](README.assets/image-20220224212736166.png)

- 后台用户数据

![image-20220224213040949](README.assets/image-20220224213040949.png)

![image-20220224213107919](README.assets/image-20220224213107919.png)



# 网站主体设计

## 模板层

### 官网

![image-20220224215541718](README.assets/image-20220224215541718.png)

![image-20220224234510935](README.assets/image-20220224234510935.png)

![image-20220227124522944](README.assets/image-20220227124522944.png)

![image-20220224234620793](README.assets/image-20220224234620793.png)

![image-20220224234644387](README.assets/image-20220224234644387.png)



![image-20220227124829202](README.assets/image-20220227124829202.png)

- 导航栏作为一个basic，被其他页面继承。
- 登录前后导航栏展示的内容是有差别的。

![image-20220224214103042](README.assets/image-20220224214103042.png)

登录前：

![image-20220225000852805](README.assets/image-20220225000852805.png)



登录后：

![image-20220225000909795](README.assets/image-20220225000909795.png)

### 侧边栏

最新文章/最热文章/搜索等

![image-20220225001021015](README.assets/image-20220225001021015.png)

![image-20220225002335156](README.assets/image-20220225002335156.png)



### 首页内容

- 首页是导航栏第一个home选项

![image-20220224214320369](README.assets/image-20220224214320369.png)

![image-20220227124702310](README.assets/image-20220227124702310.png)

### 分类页

![image-20220224214731406](README.assets/image-20220224214731406.png)

![网页捕获_24-2-2022_233936_127.0.0.1](README.assets/网页捕获_24-2-2022_233936_127.0.0.1.jpeg)

### 搜索页

![image-20220224215036438](README.assets/image-20220224215036438.png)

![网页捕获_24-2-2022_234041_127.0.0.1](README.assets/网页捕获_24-2-2022_234041_127.0.0.1.jpeg)

### 我的收藏页

![image-20220224215135164](README.assets/image-20220224215135164.png)

![image-20220227124916008](README.assets/image-20220227124916008.png)



### 我的文章页

![image-20220224215201585](README.assets/image-20220224215201585.png)

![image-20220227124939521](README.assets/image-20220227124939521.png)

### 文章详情页

![image-20220224215249689](README.assets/image-20220224215249689.png)

![网页捕获_24-2-2022_234332_127.0.0.1](README.assets/网页捕获_24-2-2022_234332_127.0.0.1.jpeg)



## 视图层

### 首页

![image-20220224234901554](README.assets/image-20220224234901554.png)

### 分类

![image-20220224234943275](README.assets/image-20220224234943275.png)

### 文章详情

![image-20220224235005620](README.assets/image-20220224235005620.png)

### 搜索展示

![image-20220224235045165](README.assets/image-20220224235045165.png)

### 收藏的文章

![image-20220224235131351](README.assets/image-20220224235131351.png)

### 用户自己的文章

![image-20220224235159045](README.assets/image-20220224235159045.png)

### 收藏以及取消收藏

![image-20220224235225130](README.assets/image-20220224235225130.png)

## 模型层

### 文章分类模型

![image-20220224235448892](README.assets/image-20220224235448892.png)

![image-20220227125040215](README.assets/image-20220227125040215.png)



### 文章标签模型

![image-20220224235515844](README.assets/image-20220224235515844.png)

![image-20220225000514920](README.assets/image-20220225000514920.png)

![image-20220225000534189](README.assets/image-20220225000534189.png)



### 文章模型

![image-20220224235918150](README.assets/image-20220224235918150.png)

![image-20220225000556514](README.assets/image-20220225000556514.png)

![image-20220225000639178](README.assets/image-20220225000639178.png)

![image-20220225000653628](README.assets/image-20220225000653628.png)



### 侧边栏模型

![image-20220224235851961](README.assets/image-20220224235851961.png)

![image-20220224235617159](README.assets/image-20220224235617159.png)

![image-20220224235705578](README.assets/image-20220224235705578.png)

![image-20220224235717141](README.assets/image-20220224235717141.png)

![image-20220225000127759](README.assets/image-20220225000127759.png)

![image-20220225000149717](README.assets/image-20220225000149717.png)



## 表单

### 登陆注册表单

![image-20220225002528839](README.assets/image-20220225002528839.png)

```python
"""
用户账户相关的功能：注册、登录、注销
"""
from django import forms
from rusSta import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from utils import encrypt
from rusSta.forms.bootstrap import BootStrapForm
from rusSta.views import account


class RegisterModelForm(BootStrapForm, forms.ModelForm):
    # django里面没有专门针对手机号的验证，在这里可以重写
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])

    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=30,
        error_messages={
            'min_length': "密码长度不能小于8个字符",
            'max_length': "密码长度不能大于30个字符"
        },
        widget=forms.PasswordInput()
    )
    # 重复密码验证
    confirm_password = forms.CharField(
        label='重复密码',
        min_length=8,
        max_length=30,
        error_messages={
            'min_length': "重复密码长度不能小于8个字符",
            'max_length': "重复密码长度不能大于30个字符"
        },
        widget=forms.PasswordInput())

    class Meta:
        model = models.UserInfo
        fields = ['username', 'email', 'mobile_phone', 'password', 'confirm_password']

    def clean_username(self):
        username = self.cleaned_data['username']
        exists = models.UserInfo.objects.filter(username=username).exists()
        if exists:
            raise ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        exists = models.UserInfo.objects.filter(email=email).exists()  # 可能有问题
        if exists:
            raise ValidationError('邮箱已存在')
        return email

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('手机号已注册')
        return mobile_phone

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密并返回
        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data['password']
        confirm_pwd = encrypt.md5(self.cleaned_data['confirm_password'])
        if pwd != confirm_pwd:
            raise ValidationError('两次密码不一致')
        return confirm_pwd


class LoginForm(BootStrapForm, forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput(render_value=True))
    code = forms.CharField(label='图片验证码')

    class Meta:
        fields = ['username', 'password', 'code']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    #
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     return username

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密并返回
        return encrypt.md5(pwd)

    def clean_code(self):
        """图片验证码是否正确"""
        # 读取用户输入的验证码
        code = self.cleaned_data['code']
        # 去session获取自己的验证码

        session_code = self.request.session.get('image_code')
        # if not session_code:
        #     raise ValidationError('验证码已过期，请重新获取')
        if code.strip().upper() != session_code.strip().upper():
            raise ValidationError('验证码输入错误')

        return code

```

## 中间件

控制登录/未登录状态

![image-20220225002700513](README.assets/image-20220225002700513.png)

## 富文本编辑器

富文本编辑器插件

![image-20220225003056566](README.assets/image-20220225003056566.png)

后台集成富文本编辑器

![image-20220225003207807](README.assets/image-20220225003207807.png)

# 版本控制

- 生成一个requirements.txt文件，，，把当前文件中所有的模块放入requirements.txt
- pip freeze > requirements.txt

![image-20220116142622784](README.assets/image-20220116142622784.png)



![image-20220225003401921](README.assets/image-20220225003401921.png)



# 项目部署

暂未完成。

- 首先我尝试了ubuntu+nginx+uwsgi方法进行部署
  - 在ubuntu中升级python3.7 
  - 更新pip
  - 下载russta项目
  - pip freeze > requirements.txt 安装依赖 (部分装不上去)
  - 运行django项目（失败）
- 更换方法  宝塔面板+Nginx+uwsgi+mysql快速部署
  - Ubuntu中安装宝塔面板
  - 宝塔面板中下载nginx mysql  
  - 建立网站（失败） 暂时没找到宝塔面板不好使的原因



由于尝试多种办法失败，暂时搁置对项目的部署。
