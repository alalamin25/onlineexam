# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0012_auto_20160224_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mcq_question',
            options={'permissions': (('can_view_odd_ids', 'can_view_odd_ids'), ('can_view_even_ids', 'can_view_even_ids'))},
        ),
    ]
