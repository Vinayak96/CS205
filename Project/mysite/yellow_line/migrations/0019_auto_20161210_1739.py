# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yellow_line', '0018_auto_20161210_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
