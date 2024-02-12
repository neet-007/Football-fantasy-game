# Generated by Django 4.2.10 on 2024-02-12 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0006_gameweekplayer_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameweekplayer',
            name='game_week_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_week_player_game_week_team', to='team_management.gameweekteam'),
        ),
        migrations.AlterField(
            model_name='gameweekteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_week_team_team', to='team_management.team'),
        ),
    ]