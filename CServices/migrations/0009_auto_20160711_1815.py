# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CServices', '0008_auto_20160711_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidrequest',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wiprequest',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
