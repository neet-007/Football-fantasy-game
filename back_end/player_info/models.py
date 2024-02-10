from django.db import models
from user_auth.models import TeamsChoices
# Create your models here.

MIN_PLAYER_PRICE_CHANGE = 0.1
MAX_PLAYER_PRICE_CHANGE = 0.3
class PlayerPositions(models.IntegerChoices):
    GK = 0, 'GoalKeeper'
    DF = 1, 'Defender'
    MF = 3, 'Midfielder'
    ST = 4, 'Striker'

class Player(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    nation = models.CharField(max_length=10, null=True)
    position = models.IntegerField(choices=PlayerPositions.choices, db_index=True)
    age = models.IntegerField(default=0, null=True)
    matches_played = models.IntegerField(default=0, null=True)
    starts = models.IntegerField(default=0, null=True)
    minutes = models.IntegerField(default=0, null=True, db_index=True)
    nineties = models.DecimalField(max_digits=6, decimal_places=1, default=0, null=True)
    goals = models.IntegerField(default=0, null=True, db_index=True)
    assists = models.IntegerField(default=0, null=True, db_index=True)
    goals_and_assists = models.IntegerField(default=0, null=True)
    none_penalty_goals = models.IntegerField(default=0, null=True)
    penalty_goals = models.IntegerField(default=0, null=True, db_index=True)
    penalties_attempted = models.IntegerField(default=0, null=True, db_index=True)
    yellow_cards = models.IntegerField(default=0, null=True, db_index=True)
    red_cards = models.IntegerField(default=0, null=True, db_index=True)
    team = models.IntegerField(choices=TeamsChoices.choices, db_index=True)
    saves = models.IntegerField(default=0)
    penalty_saves = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0, db_index=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True)
    overall_points = models.IntegerField(default=0)
    game_week_points = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f'{self.last_name} {self.position} {self.team}'

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