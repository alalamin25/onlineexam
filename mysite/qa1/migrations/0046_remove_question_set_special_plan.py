# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-23 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0045_auto_20160522_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_set',
            name='special_plan',
        ),
    ]
