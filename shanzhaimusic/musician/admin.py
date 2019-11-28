from django.contrib import admin

# Register your models here.
from .models import Musician


class MusicianAdmin(admin.ModelAdmin):
    # 设置每页显示条数
    list_per_page = 10
    # 显示那些键
    list_display = ['id', 'musician', 'music_name', 'music', 'style', 'picture', 'like', 'addtime']
    # 哪个有超链接
    list_display_links = ['id']
    # 过滤器
    list_filter = ['musician', 'style', ]
    # 哪个可以直接编辑
    list_editable = ['musician', 'music_name', 'music', 'style', 'picture', 'like', ]


# class testAdmin(admin.ModelAdmin):
#   list_display = ('a_name','b_level','...')
#     actions = ["export_excel",]
#     export_excel.short_description = "导出Excel文件"

admin.site.register(Musician, MusicianAdmin)
# 把"Django 管理"换掉
admin.site.site_header = "后台管理"
