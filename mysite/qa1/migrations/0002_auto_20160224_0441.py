# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq_question',
            name='choice_a',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choice_b',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choice_c',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choice_d',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='mcq_answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
