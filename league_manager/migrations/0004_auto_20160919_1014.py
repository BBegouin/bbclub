# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-19 10:14
from __future__ import unicode_literals

from django.db import migrations
from league_manager.models.club import Club
from league_manager.models.league import League

def init_club_and_league(apps, schema_editor):

    new_club = Club(name = "Cocgnac")
    new_club.save()

    new_league = League(name = "saison 2016 - 2017", Club = new_club)
    new_league.save()


class Migration(migrations.Migration):

    dependencies = [
        ('league_manager', '0003_auto_20160916_0829'),
    ]

    operations = [
        migrations.RunPython(init_club_and_league),
    ]
