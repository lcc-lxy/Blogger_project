from django.db import models
# Create your models here.
from users.models import User
import flask


# import

class Music(models.Model):

    music_name = models.CharField(max_length=64,verbose_name='歌名')

    singer = models.CharField(max_length=24,verbose_name='歌手')

    music_dir = models.CharField(max_length=128,verbose_name='歌曲路径')

    kind = models.CharField(max_length=8,verbose_name='歌曲分类')

    discuss_user = models.ManyToManyField(User)

