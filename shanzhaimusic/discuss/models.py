from django.db import models

# Create your models here.
from music.models import Music
from users.models import User


class Discuss(models.Model):

    message = models.TextField(verbose_name='评论内容')

    user_id = models.ForeignKey(User)

    music_id = models.ForeignKey(Music)

    parent_id = models.IntegerField(default=0,verbose_name='父评论ID')

    created_time = models.DateTimeField(auto_now=True,verbose_name='评论时间')



