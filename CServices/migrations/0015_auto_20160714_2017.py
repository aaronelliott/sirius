# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CServices', '0014_auto_20160714_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidrequest',
            name='p_num',
            field=models.IntegerField(unique=True),
        ),
    ]
