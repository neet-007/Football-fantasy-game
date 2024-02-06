from django.db import models
from user_auth.models import TeamsChoices
# Create your models here.

class PlayerPositions(models.IntegerChoices):
    GK = 0, 'GoalKeeper'
    DF = 1, 'Defender'
    MF = 3, 'Midfielder'
    ST = 4, 'Striker'

class Player(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    nation = models.CharField(max_length=10, null=True)
    position = models.IntegerField(choices=PlayerPositions.choices)
    age = models.IntegerField(default=0, null=True)
    matches_played = models.IntegerField(default=0, null=True)
    starts = models.IntegerField(default=0, null=True)
    minutes = models.IntegerField(default=0, null=True)
    nineties = models.DecimalField(max_digits=6, decimal_places=1, default=0, null=True)
    goals = models.IntegerField(default=0, null=True)
    assists = models.IntegerField(default=0, null=True)
    goals_and_assists = models.IntegerField(default=0, null=True)
    none_penalty_goals = models.IntegerField(default=0, null=True)
    penalty_goals = models.IntegerField(default=0, null=True)
    penalties_attempted = models.IntegerField(default=0, null=True)
    yellow_cards = models.IntegerField(default=0, null=True)
    red_cards = models.IntegerField(default=0, null=True)
    team = models.IntegerField(choices=TeamsChoices.choices)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    overall_points = models.IntegerField(default=0)
    game_week_points = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f'{self.name} {self.position}'

class PlayerIjuriesAndBansStatusChoices(models.IntegerChoices):
    CHANCE_25 = 0, '25% Chance of playing'
    CHANCE_50 = 1, '50% Chance of playing'
    CHANCE_75 = 2, '70% Chance of playing'
    INJURED = 3, 'Injured'
    SUSPENDED = 4, 'Suspended'

class PlayerIjuriesAndBans(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    team = models.IntegerField(choices=TeamsChoices.choices)
    status = models.IntegerField(null=True)
    return_data = models.DateField(null=True)