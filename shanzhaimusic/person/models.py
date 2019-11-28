from django.db import models

# Create your models here.
from users.models import User


class Person_diary(models.Model):
    diary_id = models.AutoField(verbose_name='编号',primary_key=True,auto_created=True,max_length=20)
    user_id = models.ForeignKey(User)
    content = models.CharField(verbose_name='日记内容',max_length=500)
    created_time = models.DateTimeField(auto_now_add=True,max_length=30,verbose_name='创建时间')

    class Meta():
        db_table = 'person_diary'


class Person_photo(models.Model):
    photo_id = models.AutoField(verbose_name='照片编号',primary_key=True,auto_created=True,max_length=20)
    user_id = models.ForeignKey(User)
    avatar = models.ImageField(upload_to='avatar', default='', verbose_name='头像')

    class Meta():
        db_table = 'person_photo'


