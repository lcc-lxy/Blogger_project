# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-06 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='login_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='用户登录时间'),
        ),
    ]