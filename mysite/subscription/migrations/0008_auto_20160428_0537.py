# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 05:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 28, 5, 37, 15, 41715, tzinfo=utc), verbose_name='Request Date: '),
        ),
    ]