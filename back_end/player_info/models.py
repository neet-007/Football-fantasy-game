from django.db import models
from user_auth.models import TeamsChoices
# Create your models here.

class PlayerPositions(models.IntegerChoices):
    GK = 0, 'GoalKeeper'
    DF = 1, 'Defender'
    MF = 3, 'Midfielder'
    ST = 4, 'Striker'

class Player(models.Model):
    name = models.CharField(max_length=255)
    nation = models.CharField(max_length=10)
    position = models.IntegerField(choices=PlayerPositions.choices)
    age = models.IntegerField()
    matches_played = models.IntegerField()
    starts = models.IntegerField()
    minutes = models.IntegerField()
    nineties = models.DecimalField(max_digits=6, decimal_places=1)
    goals = models.IntegerField()
    assists = models.IntegerField()
    goals_and_assists = models.IntegerField()
    none_penalty_goals = models.IntegerField()
    penalty_goals = models.IntegerField()
    penalties_attempted = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    team = models.IntegerField(choices=TeamsChoices.choices)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    overall_points = models.IntegerField(default=0)
    game_week_points = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f'{self.name} {self.position}'