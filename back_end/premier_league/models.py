from typing import Iterable
from django.db import models
from player_info.models import TeamsChoices
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class PremierLeagueTeam(models.Model):
    name = models.CharField(max_length=40)
    team_code = models.PositiveIntegerField(choices=TeamsChoices.choices)
    postition = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1), MaxValueValidator(20)])
    matches_played = models.PositiveIntegerField(validators=[MaxValueValidator(38)])
    wins = models.PositiveIntegerField(validators=[MaxValueValidator(38)], default=0)
    losses = models.PositiveIntegerField(validators=[MaxValueValidator(38)], default=0)
    draws = models.PositiveIntegerField(validators=[MaxValueValidator(38)], default=0)
    goals_for = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)
    goals_differance = models.IntegerField(default=0)
    points = models.PositiveIntegerField(validators=[MaxValueValidator(114)], default=0)
    points_per_match = models.FloatField(default=0)
    expected_goals_for = models.FloatField(default=0)
    expected_goals_against = models.FloatField(default=0)
    expected_goals_differance = models.FloatField(default=0)
    expected_goals_differance_per_ninety = models.FloatField(default=0)
    last_five = models.CharField(max_length=10)

    def save(self, *args, **kwargs) -> None:
        if self.matches_played != self.wins + self.draws + self.losses:
            raise ValidationError('wins + losses + draws must equal games played')
        if (self.goals_for - self.goals_against) != self.goals_differance:
            raise ValidationError('goals for + goals againts must equal goal differance')
        if self.name == 'arsenal':
            self.team_code = 0
        if self.name == 'aston villa':
            self.team_code = 1
        if self.name == 'brentford':
            self.team_code = 2
        if self.name == 'brighton':
            self.team_code = 3
        if self.name == 'bournemouth':
            self.team_code = 4
        if self.name == 'burnley':
            self.team_code = 5
        if self.name == 'chelsea':
            self.team_code = 6
        if self.name == 'crystal palace':
            self.team_code = 7
        if self.name == 'everton':
            self.team_code = 8
        if self.name == 'fulham':
            self.team_code = 9
        if self.name == 'liverpool':
            self.team_code = 10
        if self.name == 'luton town':
            self.team_code = 11
        if self.name == 'manchester city':
            self.team_code = 12
        if self.name == 'manchester utd':
            self.team_code = 13
        if self.name == 'newcastle utd':
            self.team_code = 14
        if self.name == "nott'ham forest":
            self.team_code = 15
        if self.name == 'sheffield utd':
            self.team_code = 16
        if self.name == 'tottenham':
            self.team_code = 17
        if self.name == 'west ham':
            self.team_code = 18
        if self.name == 'wolves':
            self.team_code = 19
        return super().save(*args, **kwargs)

class GroundChoices(models.IntegerChoices):
    HOME = 0, 'Home Game'
    AWAY = 1, 'Away Game'

class DayChoices(models.IntegerChoices):
    SATURDAY = 0, 'Saturday'
    SUNDAY = 1, 'Sunday'
    MONDAY = 2, 'Monday'
    TUESDAY = 3, 'Tuesday'
    WEDNESDAY = 4, 'Wednesday'
    THURSDAY = 5, 'Thursday'
    FRIDAY = 6, 'Friday'

class ResultChoices(models.IntegerChoices):
    WIN = 0, 'Win'
    LOSE = 1, 'Lose'
    DRAW = 2, 'Draw'

class TeamFixtures(models.Model):
    team = models.PositiveIntegerField(choices=TeamsChoices.choices)
    date = models.DateField()
    comp = models.PositiveIntegerField()
    game_week = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(38)])
    day = models.PositiveIntegerField(choices=DayChoices.choices)
    ground = models.PositiveIntegerField(choices=GroundChoices.choices)
    result = models.PositiveIntegerField(choices=ResultChoices.choices, null=True)
    goals_for = models.PositiveIntegerField(default=None, null=True)
    goals_against = models.PositiveIntegerField(default=None, null=True)
    opponent = models.PositiveIntegerField(choices=TeamsChoices.choices)

    def save(self, *args, **kwargs) -> None:
        if self.team == self.opponent:
            raise ValidationError('team cant be oppoent team')
        return super().save(*args, **kwargs)