# Generated by Django 4.2.10 on 2024-02-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
