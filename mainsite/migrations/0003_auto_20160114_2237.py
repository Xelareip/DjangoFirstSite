# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='mainsite/default_post.html', max_length=200, verbose_name='Static address'),
        ),
    ]
