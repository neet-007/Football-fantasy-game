from collections.abc import Iterable
from django.db import models
from team_management.models import Team
from django.core.exceptions import ValidationError
# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=125, db_index=True)
    owner = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='league_owner')
    admin = models.ManyToManyField(Team, related_name='league_admin')
    num_of_players = models.PositiveIntegerField(default=0)
    is_h2h = models.BooleanField(default=False, db_index=True)

    def save(self, *args, **kwargs) -> None:
        self.num_of_players = self.leagueteam_set.all().count()
        return super().save(*args, **kwargs)

class LeagueTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1)
    game_week_points = models.PositiveIntegerField(default=0, db_index=True)
    overall_points = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    #figure out how to auto sort when score changees
    def save(self, *args, **kwargs) -> None:
        if self.league.is_h2h:
            raise ValidationError('this league is h2h')
        if self.position > self.league.num_of_players:
            raise ValidationError('position cant be more than the num of players in league')
        self.game_week_points = self.team.gameweekteam.points
        self.overall_points = self.team.overall_points
        return super().save(*args, **kwargs)

class H2HLeagueTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)
    games_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0, db_index=True)
    losses = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    game_week_points = models.PositiveIntegerField(default=0, db_index=True)
    score = models.PositiveIntegerField(default=0, db_index=True)
    overall_points = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    #figure out how to auto sort when score changees
    def save(self, *args, **kwargs) -> None:
        if not self.league.is_h2h:
            raise ValidationError('league is not h2h')
        if self.position > self.league.num_of_players:
            raise ValidationError('player position cant be more than league number of players')
        if self.wins + self.draws + self.losses != self.games_played:
            raise ValidationError('number of wins and draws and losses must equal games played')
        if (self.wins * 3) + (self.draws) != self.score:
            raise ValidationError('wins + draws must equal score')
        self.game_week_points = self.team.gameweekteam.points
        self.overall_points = self.team.overall_points
        return super().save(*args, **kwargs)

#implement later
class cup(models.Model):
    pass