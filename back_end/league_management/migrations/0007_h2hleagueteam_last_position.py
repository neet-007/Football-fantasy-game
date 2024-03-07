# Generated by Django 4.2.10 on 2024-03-07 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_management', '0006_leagueteam_last_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='h2hleagueteam',
            name='last_position',
            field=models.PositiveBigIntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
