# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-06 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_userprofile_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='login_time',
            field=models.DateTimeField(null=True, verbose_name='用户登录时间'),
        ),
    ]