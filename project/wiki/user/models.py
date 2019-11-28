import random

from django.db import models

# Create your models here.
def default_sign():
    signs = ['葫芦娃','奥特曼','小怪兽']
    return random.choice(signs)
class Userprofile(models.Model):
    username = models.CharField(max_length=11,verbose_name='用户名',primary_key=True)
    nickname = models.CharField(max_length=30,verbose_name='昵称')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    password = models.CharField(max_length=32,verbose_name='密码')
    sign = models.CharField(max_length=150,verbose_name='个人签名',default=default_sign)
    info = models.CharField(max_length=150,verbose_name='个人描述')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    #upload_to 指定储存位置  MEDIA_ROOT+UPLOAD_TO的位置  wiki/media/avatar
    avatar = models.ImageField(upload_to='avatar',default='',verbose_name='头像')
    login_time = models.DateTimeField(verbose_name='用户登录时间',null=True)
    score = models.IntegerField(verbose_name='分数',null=True,default=0)
    class Meta():
        db_table = 'user_profile'
    def __str__(self):
        return self.username+self.sign
