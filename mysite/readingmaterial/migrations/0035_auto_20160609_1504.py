# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-09 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingmaterial', '0034_auto_20160603_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quick_question',
            name='quick_question_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
