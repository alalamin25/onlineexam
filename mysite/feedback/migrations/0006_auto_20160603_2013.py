# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-03 14:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_remove_report_url'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set([('user', 'quick_question', 'mcq_question')]),
        ),
    ]