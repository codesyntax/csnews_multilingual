# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-25 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csnews_multilingual', '0005_auto_20161117_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagtranslation',
            name='slug',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]