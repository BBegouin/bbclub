# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-06 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league_manager', '0028_auto_20161105_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerreport',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league_manager.Player'),
        ),
    ]
