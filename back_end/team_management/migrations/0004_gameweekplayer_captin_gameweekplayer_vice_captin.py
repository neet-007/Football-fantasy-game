# Generated by Django 4.2.10 on 2024-03-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0003_gameweekplayer_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameweekplayer',
            name='captin',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='gameweekplayer',
            name='vice_captin',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]