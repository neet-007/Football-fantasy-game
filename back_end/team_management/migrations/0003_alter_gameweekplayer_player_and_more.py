# Generated by Django 4.2.10 on 2024-02-09 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player_info', '0002_alter_player_assists_alter_player_goals_and_more'),
        ('team_management', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameweekplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_info.player'),
        ),
        migrations.AlterField(
            model_name='gameweekplayer',
            name='points',
            field=models.IntegerField(db_index=True, default=None),
        ),
    ]
