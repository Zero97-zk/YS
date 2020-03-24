from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField('用户名', max_length=20, unique=True)
    nickname = models.CharField('昵称', max_length=30, null=True)
    password = models.CharField('密码', max_length=40)
    email = models.EmailField('邮箱')
    phone = models.CharField('手机号码', max_length=11)
    description = models.CharField('描述', max_length=200, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    login_time = models.CharField('最近一次登陆时间', max_length=12, default='')
    # image字段
    # upload_to 存储文件夹 settings.py MEDIA_ROOT + upload_to
    avatar = models.ImageField('头像', upload_to='avatar/', null=True)

    class Meta:
        db_table = 'user'
