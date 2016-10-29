# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-17 08:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('league_manager', '0009_auto_20161002_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='coach',
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Coach'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playerevolution',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evolution', to='league_manager.Player'),
        ),
    ]
