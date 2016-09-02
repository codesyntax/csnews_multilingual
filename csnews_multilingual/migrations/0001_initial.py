# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photologue', '0014_auto_20160609_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('published', models.DateTimeField(verbose_name='Published')),
                ('is_public', models.BooleanField(default=True, verbose_name='Is public')),
                ('added', models.DateField(auto_now_add=True, verbose_name='Added')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_images', to='photologue.Photo')),
            ],
            options={
                'get_latest_by': 'published',
                'ordering': ('-published',),
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('summary', models.TextField(blank=True, verbose_name='Summary')),
                ('body', models.TextField(verbose_name='Body')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='csnews_multilingual.Article')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'csnews_multilingual_article_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
