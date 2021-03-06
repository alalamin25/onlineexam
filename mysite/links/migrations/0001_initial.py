# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 13:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(blank=True, max_length=200, null=True)),
                ('link_text', models.TextField(blank=True, max_length=200, null=True, verbose_name='Notice ')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Publishing Date: ')),
                ('edit_date', models.DateTimeField(blank=True, null=True, verbose_name='Editing Date: ')),
                ('link_url_1', models.TextField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 ')),
                ('video_url_1', models.TextField(blank=True, max_length=200, null=True, verbose_name='Link URL 1 ')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/link/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/link/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/link/')),
                ('file1', models.FileField(blank=True, null=True, upload_to='files/link/')),
                ('file2', models.FileField(blank=True, null=True, upload_to='files/link/')),
                ('file3', models.FileField(blank=True, null=True, upload_to='files/link/')),
            ],
            options={
                'verbose_name': 'Link',
            },
        ),
        migrations.CreateModel(
            name='Link_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_topic_text', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Link Topic List',
            },
        ),
        migrations.AddField(
            model_name='link',
            name='link_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='links.Link_Topic'),
        ),
        migrations.AddField(
            model_name='link',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
