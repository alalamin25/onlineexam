# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_url_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
        migrations.AddField(
            model_name='link',
            name='link_url_3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
        migrations.AddField(
            model_name='link',
            name='link_url_4',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
        migrations.AddField(
            model_name='link',
            name='link_url_5',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
        migrations.AddField(
            model_name='link',
            name='video_url_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
        migrations.AddField(
            model_name='link',
            name='video_url_3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
        migrations.AlterField(
            model_name='link',
            name='link_url_1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
        migrations.AlterField(
            model_name='link',
            name='video_url_1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 '),
        ),
    ]