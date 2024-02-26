# Generated by Django 4.2.10 on 2024-02-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier_league', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamfixtures',
            options={'ordering': ['-game_week']},
        ),
        migrations.AddField(
            model_name='teamfixtures',
            name='time',
            field=models.TimeField(db_index=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teamfixtures',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]