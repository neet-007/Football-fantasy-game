from collections.abc import Iterable
from django.db import models, transaction
from team_management.models import Team
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

class LeagueManager(models.Manager):

    def create(self, name:str, owner:'Team', admin:list[int]=[], is_h2h:bool=False, starting_game_week:int=1, allow_post_create_entry:bool=True) -> 'League':
        if len(admin) > 0:
            pass

        league_instance = League(name=name, owner=owner, is_h2h=is_h2h, starting_game_week=starting_game_week, allow_post_create_entry=allow_post_create_entry)
        league_instance.save()

        if is_h2h:
            self.add_h2h_league_team(h2h_league_pk=league_instance.pk, team=owner.pk)
        else:
            self.add_league_team(league_instance.pk, owner.pk)
        return league_instance

    def sort_league(self, league_pk:int) -> bool:
        try:
            try:
                league = self.get(pk=league_pk, is_h2h=False)
            except League.DoesNotExist:
                raise ValueError('leagu not found')

            with transaction.atomic():
                teams = LeagueTeam.objects.filter(league=league)
                if league.num_of_players == 0:
                    return False

                teams_update = []
                for i in range(len(teams)):
                    teams[i].position = i
                    teams_update.append(teams[i])

                LeagueTeam.objects.bulk_update(teams_update, fields=['position'])
        except:
            pass

    def sort_h2h_league(self, h2h_league_pk:int):
        try:
            try:
                league = self.get(pk=h2h_league_pk, is_h2h=True)
            except League.DoesNotExist:
                raise ValueError('leagu not found')

            with transaction.atomic():
                teams = H2HLeagueTeam.objects.filter(league=league)
                if league.num_of_players == 0:
                    return False

                teams_update = []
                for i in range(len(teams)):
                    teams[i].position = i
                    teams_update.append(teams[i])

                H2HLeagueTeam.objects.bulk_update(teams_update, fields=['position'])
        except:
            pass

    def add_league_team(self, league_pk:int, team:int) -> 'LeagueTeam':
        try:
            league = self.get(pk=league_pk, is_h2h=False)
        except League.DoesNotExist:
            raise ValueError('league not found')

        try:
            team_instance = Team.objects.get(pk=team)
        except Team.DoesNotExist:
            raise ValueError('team not found')

        if LeagueTeam.objects.filter(team=team_instance, league=league).exists():
            raise ValueError('team is already in this league')

        league.num_of_players += 1
        league.save()

        league_team = LeagueTeam.objects.create(team=team_instance, league=league)
        self.sort_league(league_pk=league_pk)

        return league_team

    def add_h2h_league_team(self, h2h_league_pk:int, team:int) -> 'H2HLeagueTeam':
        try:
            league = self.get(pk=h2h_league_pk, is_h2h=True)
        except League.DoesNotExist:
            raise ValueError('league not found')

        try:
            team_instance = Team.objects.get(pk=team)
        except Team.DoesNotExist:
            raise ValueError('team not found')

        if H2HLeagueTeam.objects.filter(team=team, league=league).exists():
            raise ValueError('team is already in this league')

        league.num_of_players += 1
        league.save()

        h2h_team = H2HLeagueTeam.objects.create(team=team_instance, league=league)
        self.sort_h2h_league(h2h_league_pk=h2h_league_pk)

        return h2h_team

    def remove_league_team(self, league_team:'LeagueTeam', league_pk:int):
        league_team.delete()
        self.sort_league(league_pk=league_pk)

    def remove_h2h_league_team(self,h2h_league_team:'H2HLeagueTeam', h2h_league_pk:int):
        h2h_league_team.delete()
        self.sort_h2h_league(h2h_league_pk=h2h_league_pk)


class League(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    owner = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='league_owner')
    admin = models.ManyToManyField(Team, related_name='league_admin')
    num_of_players = models.PositiveIntegerField(default=0)
    is_h2h = models.BooleanField(default=False, db_index=True)
    starting_game_week = models.PositiveIntegerField(default=1, blank=True, validators=[MinValueValidator(1), MaxValueValidator(38)])
    allow_post_create_entry = models.BooleanField(default=True, blank=True)

    objects = LeagueManager()

class LeagueTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1, blank=True, validators=[MinValueValidator(1)])
    game_week_points = models.IntegerField(default=0, db_index=True, blank=True)
    overall_points = models.IntegerField(default=0, blank=True)
    """
    class Meta:
        ordering = ['-overall_points']
    """
    #figure out how to auto sort when score changees
    def save(self, *args, **kwargs) -> None:
        if self.position > self.league.num_of_players:
            raise ValidationError(f'position cant be more than the num of players in league pos:{self.position} player:{self.league.num_of_players}')
        try:
            self.game_week_points = self.team.game_week_team_team.points
        except AttributeError:
            self.game_week_points = 0

        self.overall_points = self.team.overall_points
        League.objects.sort_league(league_pk=self.league.pk)
        return super().save(*args, **kwargs)

class H2HLeagueTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1, blank=True, validators=[MinValueValidator(1)])
    games_played = models.PositiveIntegerField(default=0, blank=True)
    wins = models.PositiveIntegerField(default=0, db_index=True, blank=True)
    losses = models.PositiveIntegerField(default=0, blank=True)
    draws = models.PositiveIntegerField(default=0, blank=True)
    game_week_points = models.IntegerField(default=0, db_index=True, blank=True)
    score = models.PositiveIntegerField(default=0, db_index=True, blank=True)
    overall_points = models.IntegerField(default=0, blank=True)
    """
    class Meta:
        ordering = ['-score']
    """
    #figure out how to auto sort when score changees
    def save(self, *args, **kwargs) -> None:
        if self.position > self.league.num_of_players:
            raise ValidationError(f'player position cant be more than league number of players pos:{self.position} players:{self.league.num_of_players}')
        if self.wins + self.draws + self.losses != self.games_played:
            raise ValidationError('number of wins and draws and losses must equal games played')
        if (self.wins * 3) + (self.draws) != self.score:
            raise ValidationError('wins + draws must equal score')
        try:
            self.game_week_points = self.team.game_week_team_team.points
        except AttributeError:
            self.game_week_points = 0

        self.overall_points = self.team.overall_points
        League.objects.sort_h2h_league(h2h_league_pk=self.league.pk)
        return super().save(*args, **kwargs)


#implement later
class cup(models.Model):
    pass