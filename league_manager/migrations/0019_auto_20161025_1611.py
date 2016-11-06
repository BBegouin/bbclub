# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-25 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_manager', '0018_auto_20161025_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamreport',
            name='fame',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teamreport',
            name='fan_factor',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teamreport',
            name='other_casualties',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teamreport',
            name='supporters',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teamreport',
            name='winnings',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]