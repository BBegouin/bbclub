# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-21 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_manager', '0015_auto_20161021_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamreport',
            name='other_casualties',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
