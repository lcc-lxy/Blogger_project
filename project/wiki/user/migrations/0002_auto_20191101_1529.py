# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-01 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
