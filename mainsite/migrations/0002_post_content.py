# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.URLField(default='mainsite/default_post.html', verbose_name='Address'),
        ),
    ]
