# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-06 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191106_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='login_time',
        ),
    ]
