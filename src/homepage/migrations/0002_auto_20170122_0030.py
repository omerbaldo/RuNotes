# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='info',
            field=models.TextField(max_length=4000, null=True),
        ),
    ]