# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readingmaterial', '0014_auto_20160307_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentmarkedmcq',
            name='content',
        ),
    ]
