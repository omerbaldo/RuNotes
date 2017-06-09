# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20170122_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='display_info',
            field=models.TextField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='posts/'),
        ),
    ]
