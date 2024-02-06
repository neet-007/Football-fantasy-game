# Generated by Django 4.2.9 on 2024-02-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='assists',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='goals_and_assists',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='matches_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='nineties',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='player',
            name='none_penalty_goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='penalties_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='penalty_goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='player',
            name='red_cards',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='starts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='yellow_cards',
            field=models.IntegerField(default=0),
        ),
    ]
