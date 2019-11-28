from django.db import models
from user.models import *
# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=50,verbose_name='文章主题')
    category = models.CharField(max_length=20,verbose_name='博客的分类')
    limit = models.CharField(max_length=10,verbose_name='权限')
    introduce = models.CharField(max_length=90,verbose_name='博客简介')
    content = models.TextField(verbose_name='博客内容')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='博客创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='博客更新时间')
    author = models.ForeignKey(Userprofile)

    class Meta():
        db_table ='topic'