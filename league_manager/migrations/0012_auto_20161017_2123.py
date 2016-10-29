# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-17 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league_manager', '0011_auto_20161017_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Injury_Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dice_value_1', models.PositiveSmallIntegerField(null=True)),
                ('dice_value_2', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerDowngrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(null=True)),
                ('injury_roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade', to='league_manager.Injury_Roll')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_pass', models.PositiveSmallIntegerField()),
                ('nb_td', models.PositiveSmallIntegerField()),
                ('nb_int', models.PositiveSmallIntegerField()),
                ('nb_cas', models.PositiveSmallIntegerField()),
                ('nb_mvp', models.PositiveSmallIntegerField()),
                ('nb_foul', models.PositiveSmallIntegerField()),
                ('nb_blocks', models.PositiveSmallIntegerField()),
                ('is_wounded', models.BooleanField()),
                ('serious_casualty', models.PositiveSmallIntegerField()),
                ('earned_xp', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerUpgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(null=True)),
                ('status', models.PositiveSmallIntegerField(null=True)),
                ('type', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='player_report',
            name='player',
        ),
        migrations.RemoveField(
            model_name='player_report',
            name='team_report',
        ),
        migrations.RemoveField(
            model_name='playerevolution',
            name='player',
        ),
        migrations.RemoveField(
            model_name='playerevolution',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='team_report',
            name='score',
        ),
        migrations.RemoveField(
            model_name='xp_roll',
            name='Values',
        ),
        migrations.RemoveField(
            model_name='xp_roll',
            name='name',
        ),
        migrations.RemoveField(
            model_name='xp_roll',
            name='player_id',
        ),
        migrations.AddField(
            model_name='player',
            name='need_upgrade',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='total_xp',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xp_roll',
            name='dice_value_1',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='xp_roll',
            name='dice_value_2',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='ref_roster_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='league_manager.Ref_Roster_Line'),
        ),
        migrations.AlterField(
            model_name='team_report',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='league_manager.Team'),
        ),
        migrations.DeleteModel(
            name='Player_Report',
        ),
        migrations.DeleteModel(
            name='PlayerEvolution',
        ),
        migrations.AddField(
            model_name='playerupgrade',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upgrade', to='league_manager.Player'),
        ),
        migrations.AddField(
            model_name='playerupgrade',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='league_manager.Ref_Skills'),
        ),
        migrations.AddField(
            model_name='playerupgrade',
            name='xp_roll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upgrade', to='league_manager.Xp_Roll'),
        ),
        migrations.AddField(
            model_name='playerreport',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league_manager.Player'),
        ),
        migrations.AddField(
            model_name='playerreport',
            name='team_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league_manager.Team_Report'),
        ),
        migrations.AddField(
            model_name='playerdowngrade',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evolution', to='league_manager.Player'),
        ),
        migrations.AddField(
            model_name='injury_roll',
            name='Player_Report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='injury_roll', to='league_manager.PlayerReport'),
        ),
        migrations.AddField(
            model_name='xp_roll',
            name='Player_Report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='xp_roll', to='league_manager.PlayerReport'),
            preserve_default=False,
        ),
    ]
