# Generated by Django 4.2.10 on 2024-02-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier_league', '0002_alter_teamfixtures_options_teamfixtures_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamfixtures',
            name='time',
            field=models.TimeField(db_index=True, null=True),
        ),
    ]
