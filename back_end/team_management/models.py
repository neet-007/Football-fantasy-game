from collections.abc import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.core.validators import MinValueValidator, MaxValueValidator
from player_info.models import Player, PlayerPositions
# Create your models here.
user_model = get_user_model()


class Team(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    overall_points = models.IntegerField(default=0, db_index=True)
    overall_rank = models.IntegerField(default=0, db_index=True)
    free_transfers = models.IntegerField(default=0)
    game_week_transfers_made = models.IntegerField(default=0)
    bank = models.DecimalField(default=100, max_digits=6, decimal_places=2)
    team_value = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    bench_boost = models.BooleanField(default=True)
    free_hit = models.BooleanField(default=True)
    triple_captin = models.BooleanField(default=True)
    wild_card = models.BooleanField(default=True)

    def save(self, *args, **kwargs) -> None:
        self.team_value = sum(player.price for player in self.gameweekteam.gameweekplayer.all())
        return super().save(*args, **kwargs)

class GameWeekTeam(models.Model):
    starting_players_gk_min = 1
    starting_players_df_min = 3
    starting_players_df_max = 5
    starting_players_mf_min = 3
    starting_players_mf_max = 5
    starting_players_st_min = 1
    starting_players_st_max = 3

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0, db_index=True)
    game_week = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(38)], db_index=True)

    def save(self, *args, **kwargs) -> None:
        starting_players = self.gameweekplayer.filter(starter=True)
        benched_players = self.gameweekplayer.filter(starter=False)
        if len(starting_players) != 11:
            raise ValidationError('team must have 11 starting players')
        if len(benched_players) != 4:
            raise ValidationError('benched players must be 4')
        if starting_players.filter(pk__in=benched_players.values_list('pk', flat=True)).exists():
            raise ValidationError('cant have the same players starting and benched')
        if benched_players.filter(position=PlayerPositions.GK).count() != self.starting_players_gk_min:
            raise ValidationError('team can only have one benched goalkeeper')
        if starting_players.filter(position=PlayerPositions.GK).count() != self.starting_players_gk_min:
            raise ValidationError(f'team can only have {self.starting_players_gk_min} starting goalkeeper')
        if not (self.starting_players_df_min <= starting_players.filter(position=PlayerPositions.DF).count() <= self.starting_players_df_max):
            raise ValidationError(f'team defenders must be between {self.starting_players_df_min} and {self.starting_players_df_max} inclusive')
        if not (self.starting_players_mf_min <= starting_players.filter(position=PlayerPositions.MF).count() <= self.starting_players_mf_max):
            raise ValidationError(f'team midfielders must be between {self.starting_players_mf_min} and {self.starting_players_mf_max} inclusive')
        if not (self.starting_players_st_min <= starting_players.filter(position=PlayerPositions.ST).count() <= self.starting_players_st_max):
            raise ValidationError(f'team strikers must be between {self.starting_players_st_min} and {self.starting_players_st_max} inclusive')
        self.points = sum(player.points for player in self.gameweekplayer.all())
        return super().save(*args, **kwargs)

class GameWeekTeamPlayerBenchedOrderChoices(models.IntegerChoices):
    GK = 0, 'Goolkeeper Bench'
    FIRST_CHOICE = 1, 'First Choice'
    SECOND_CHOCIE = 2, 'Second Choice'
    THIRD_CHOICE = 3, 'Third Choice'

class GameWeekPlayer(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    game_week_team = models.OneToOneField(GameWeekTeam, on_delete=models.CASCADE)
    starter = models.BooleanField(default=False, db_index=True)
    benched_order = models.IntegerField(default=None, null=True, choices=GameWeekTeamPlayerBenchedOrderChoices.choices)
    points = models.IntegerField(default=0, db_index=True)

class PlayerTransfer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_in = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_transfer_player_in')
    player_out = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_transfer_player_out')
    game_week = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(38)])
    points_cost = models.IntegerField(default=0)

    def save(self, *args, **kwargs) -> None:
        if self.team.bank - self.player_in.price + self.player_out.price < 0:
            raise ValidationError('player doesnt have enough money to make this transfer')
        if self.team.free_transfers == 0:
            self.points_cost = 4
        return super().save(*args, **kwargs)

"""
def validate_players_in_team(sender, **kwargs):
    team_instance = kwargs['instance']
    starting_players = team_instance.starting_players.all()
    benched_players = team_instance.benched_players.all()
    if len(starting_players) != 11:
        raise ValidationError('starting players must be 11')
    if len(benched_players) != 5:
        raise ValidationError('benched players must be 5')
    if starting_players.filter(pk__in=benched_players.values_list('pk', flat=True)).exists():
        raise ValidationError('cant have the same players starting and benched')
    if benched_players.filter(position=PlayerPositions.GK).count() != team_instance.starting_players_gk_min:
        raise ValidationError('team can only have one benched goalkeeper')
    if starting_players.filter(position=PlayerPositions.GK).count() != team_instance.starting_players_gk_min:
        raise ValidationError(f'team can only have {team_instance.starting_players_gk_min} starting goalkeeper')
    if not (team_instance.starting_players_df_min <= starting_players.filter(position=PlayerPositions.DF).count() <= team_instance.starting_players_df_max):
        raise ValidationError(f'team defenders must be between {team_instance.starting_players_df_min} and {team_instance.starting_players_df_max} inclusive')
    if not (team_instance.starting_players_mf_min <= starting_players.filter(position=PlayerPositions.MF).count() <= team_instance.starting_players_mf_max):
        raise ValidationError(f'team midfielders must be between {team_instance.starting_players_mf_min} and {team_instance.starting_players_mf_max} inclusive')
    if not (team_instance.starting_players_st_min <= starting_players.filter(position=PlayerPositions.ST).count() <= team_instance.starting_players_st_max):
        raise ValidationError(f'team strikers must be between {team_instance.starting_players_st_min} and {team_instance.starting_players_st_max} inclusive')

m2m_changed.connect(validate_players_in_team, sender=Team.starting_players.through)
"""