# Generated by Django 4.2.10 on 2024-02-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier_league', '0003_alter_teamfixtures_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamfixtures',
            name='time',
            field=models.TimeField(db_index=True),
        ),
    ]