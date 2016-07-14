# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CServices', '0011_auto_20160714_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.IntegerField()),
                ('size', models.IntegerField()),
                ('length', models.IntegerField()),
                ('bid', models.FloatField()),
                ('IR', models.IntegerField()),
                ('method', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='bidrequest',
            name='length',
        ),
        migrations.RemoveField(
            model_name='bidrequest',
            name='size',
        ),
        migrations.AddField(
            model_name='bidrequest',
            name='name',
            field=models.CharField(default='crap', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bidrequest',
            name='p_num',
            field=models.IntegerField(default=999999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bidoption',
            name='bidreq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CServices.BidRequest'),
        ),
    ]
