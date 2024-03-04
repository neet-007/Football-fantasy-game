# Generated by Django 4.2.10 on 2024-03-04 23:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0004_gameweekplayer_captin_gameweekplayer_vice_captin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameweekplayer',
            name='index',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(14)]),
        ),
    ]
