# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-23 13:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0018_auto_20160523_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 23, 13, 56, 57, 296743, tzinfo=utc), verbose_name='Request Date: '),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('user', 'subscription_plan', 'is_valid', 'is_confirmed')]),
        ),
    ]
