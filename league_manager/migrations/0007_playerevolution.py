# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-02 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league_manager', '0006_team_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(null=True)),
                ('status', models.PositiveSmallIntegerField(null=True)),
                ('type', models.PositiveSmallIntegerField()),
                ('new_skill', models.ManyToManyField(blank=True, null=True, to='league_manager.Ref_Skills')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league_manager.Player')),
            ],
        ),
    ]
