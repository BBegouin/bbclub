# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-30 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_manager', '0019_auto_20161025_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamreport',
            name='result',
            field=models.SmallIntegerField(null=True),
        ),
    ]
