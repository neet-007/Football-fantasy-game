# Generated by Django 4.2.10 on 2024-02-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier_league', '0006_teamfixtures_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamfixtures',
            name='time',
            field=models.TimeField(db_index=True, null=True),
        ),
    ]
