# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
