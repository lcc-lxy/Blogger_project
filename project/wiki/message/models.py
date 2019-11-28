from django.db import models
from user.models import *
from topic.models import *
# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=100,verbose_name='留言内容')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    parent_message = models.IntegerField(verbose_name='该留言的父留言')
    publisher_id = models.ForeignKey(Userprofile)
    topic_id = models.ForeignKey(Topic)
    class Meta():
        db_table = 'message'
