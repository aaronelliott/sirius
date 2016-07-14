# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CServices', '0012_auto_20160714_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidoption',
            name='method',
            field=models.CharField(choices=[('ROOM', 'room'), ('PHONE', 'phone'), ('ONLINE', 'online'), ('FOCUS', 'focus'), ('MIXED', 'mixed')], max_length=10),
        ),
    ]