from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=24,unique=True,verbose_name='用户名')

    password = models.CharField(max_length=24,verbose_name='密码')

    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')

    info = models.CharField(max_length=256,default='',verbose_name='个人签名')
