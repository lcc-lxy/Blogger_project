from django.db import models


# Create your models here.
class Musician(models.Model):
    musician = models.CharField(max_length=10, verbose_name='歌手')
    music_name = models.CharField(max_length=6, verbose_name='歌名')
    music = models.FileField(upload_to='static/images', verbose_name='音乐路径')
    style = models.IntegerField(verbose_name="风格",
                                choices=((1, '流行'), (2, '摇滚'), (3, '电子'),
                                         (4, '民谣'),(5, '爵士'),(6, '其他'),),default=1)
    # style=models.CharField(max_length=5,verbose_name='风格')
    picture = models.ImageField(upload_to='static/images', verbose_name='图片路径')
    like = models.IntegerField(verbose_name='喜欢')
    addtime = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    def __str__(self):
        return '<%s>' % (self.musician)

    class Meta:
        # 当前model类对应的
        db_table = 'musician'
        verbose_name = '音乐人'
        verbose_name_plural = verbose_name
