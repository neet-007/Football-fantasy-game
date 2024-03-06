from collections.abc import Iterable
from typing import Any
from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.core.validators import MinValueValidator, MaxValueValidator
from player_info.models import Player, PlayerPositions
from premier_league.models import PremierLeagueTeamBase
from traceback import print_exc
# Create your models here.
GAMEWEEK = 1

user_model = get_user_model()


class TeamManager(models.Manager):
    def create(self, user, name:str, favorite_team_pk:list[int] ) -> 'Team':
        if user == AnonymousUser:
            raise ValueError('user is anonymous')


        favorite_team = PremierLeagueTeamBase.objects.filter(pk__in=favorite_team_pk)
        if len(favorite_team) <= 0:
            raise ValidationError('must provice a favorite team')

        team = Team(user=user, name=name, favorite_team=favorite_team[0])
        team.save()

        return team


class Team(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    favorite_team = models.ForeignKey(PremierLeagueTeamBase, on_delete=models.PROTECT)
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
    made_first_team = models.BooleanField(default=False)

    objects = TeamManager()

    """
    def save(self, *args, **kwargs) -> None:
        self.team_value = sum(player.price for player in self.game_week_team_team.game_week_player_game_week_team.all())
        return super().save(*args, **kwargs)
    """

class GameWeekTeamManager(models.Manager):
    def check_team_player_positions(self, players_starters, players_benched):
        if sum(player.position == PlayerPositions.GK for player in players_starters) + sum(player.position == PlayerPositions.GK for player in players_benched) != 2 and sum(player.position == PlayerPositions.DF for player in players_starters) + sum(player.position == PlayerPositions.DF for player in players_benched) != 5 and sum(player.position == PlayerPositions.MF for player in players_starters) + sum(player.position == PlayerPositions.MF for player in players_benched) != 5 and sum(player.position == PlayerPositions.ST for player in players_starters) + sum(player.position == PlayerPositions.ST for player in players_benched) != 3:
            raise ValidationError('players structure is as follows: 2 goalkeepers, 5 defenders, 5 midfielders, 3 strikers')

    def create(self, team_pk:int, starters:list[[]:int], bench_order:dict[int, []:int], captins:dict[str, int]):
        try:
            with transaction.atomic():
                team = Team.objects.filter(pk=team_pk)

                if not team:
                    raise ValidationError('team doesnt exist')

                if len(starters) != 11 and len(bench_order) != 4:
                    raise ValidationError('startes must be 11 and benched players must be 4')

                if not team[0].made_first_team:
                    team[0].made_first_team = True
                    team[0].save()

                starters_list = [starter[0] for starter in starters]
                game_week_team = GameWeekTeam(team=team[0], game_week=GAMEWEEK)
                game_week_team.save()
                players_starters = Player.objects.filter(pk__in=starters_list)
                players_benched = Player.objects.filter(pk__in=bench_order.keys())

                self.check_team_player_positions(players_starters=players_starters, players_benched=players_benched)

                players_objectes = []
                i = 0
                captin = False
                vice_captin = True
                for player in players_starters:
                    if captins['captin'] == player.pk and not captin:
                        players_objectes.append(GameWeekPlayer(player=player, game_week_team=game_week_team, position=player.position, starter=True, index=starters[i][1], captin=True))
                        captin = True
                    elif captins['vice_captin'] == player.pk and not vice_captin:
                        players_objectes.append(GameWeekPlayer(player=player, game_week_team=game_week_team, position=player.position, starter=True, index=starters[i][1], vice_captin=False))
                        vice_captin = True
                    else:
                        players_objectes.append(GameWeekPlayer(player=player, game_week_team=game_week_team, position=player.position, starter=True, index=starters[i][1]))
                    i += 1
                i = 0
                for pk, list in bench_order.items():
                    player = players_benched.filter(pk=int(pk))[0]
                    players_objectes.append(GameWeekPlayer(player=player, game_week_team=game_week_team, position=player.position, starter=False, benched_order=list[0], index=list[1]))

                if not captin or not vice_captin:
                    raise ValidationError('a team must have a captain and vice captain')
                GameWeekPlayer.objects.bulk_create(players_objectes)

                return game_week_team
        except:
            print_exc()

    def create_team_with_transfers(self, team_pk, starters:list[[]:int], bench_order:dict[int, []:int], captins:dict[str, int], transfers_dict:dict[int, list[int, int]]):
        players_transfers = Player.objects.filter(models.Q(pk__in=[int(key) for key in transfers_dict.keys()]) | models.Q(pk__in=[l_s[0] for l_s in transfers_dict.values()]))
        if not len(players_transfers) == len(transfers_dict) * 2:
            raise ValidationError('some players are not the the database')

        try:
            team = Team.objects.get(pk=team_pk)
        except Team.DoesNotExist:
            raise ValueError('no team with this pk')

        players_out = {}
        players_in = []
        transfers_to_create = []
        for player in players_transfers:
            if not str(player.pk) in transfers_dict:
                players_out [str(player.pk)] = player
                continue
            players_in.append(player)
        for player in players_in:
            transfers_to_create.append(PlayerTransfer(team=team, player_in=player, player_out=players_out[str(transfers_dict[str(player.pk)][0])], game_week=GAMEWEEK, points_cost=transfers_dict[str(player.pk)][1]))

        self.create(team_pk=team_pk, starters=starters, bench_order=bench_order, captins=captins)

        return PlayerTransfer.objects.bulk_create(transfers_to_create)

class GameWeekTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='game_week_team_team')
    points = models.IntegerField(default=0, db_index=True, blank=True)
    game_week = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(38)], db_index=True)

    objects = GameWeekTeamManager()

class GameWeekTeamPlayerBenchedOrderChoices(models.IntegerChoices):
    GK = 0, 'Goolkeeper Bench'
    FIRST_CHOICE = 1, 'First Choice'
    SECOND_CHOCIE = 2, 'Second Choice'
    THIRD_CHOICE = 3, 'Third Choice'

class GameWeekPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    index = models.PositiveIntegerField(validators=[MaxValueValidator(14)])
    game_week_team = models.ForeignKey(GameWeekTeam, on_delete=models.CASCADE, related_name='game_week_player_game_week_team')
    position = models.IntegerField(choices=PlayerPositions.choices)
    starter = models.BooleanField(default=False, db_index=True)
    captin = models.BooleanField(default=False, blank=True)
    vice_captin = models.BooleanField(default=False, blank=True)
    benched_order = models.IntegerField(default=None, null=True, choices=GameWeekTeamPlayerBenchedOrderChoices.choices, blank=True)
    points = models.IntegerField(default=0, db_index=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if self.captin and self.vice_captin:
            return ValidationError('player cant be captin and vice captin')
        return super().save(*args, **kwargs)

class PlayerTransferManager(models.Manager):
    def create(self, player_in_pk, player_out_pk, team) -> 'PlayerTransfer':
        player_in = Player.objects.get(pk=player_in_pk)
        player_out = Player.objects.get(pk=player_out_pk)

        try:
            game_week_team = GameWeekTeam.objects.get(team=team, game_week=GAMEWEEK)
        except GameWeekTeam.DoesNotExist:
            raise ValueError('game week team not found')

        players = game_week_team.game_week_player_game_week_team.all()

        starter = False
        benched_order = None
        for player in players:
            if player == player_out:
                starter = player.starter
                benched_order = player.benched_order
                player.delete()
                break

        if starter:
            GameWeekPlayer.objects.create(player=player_in, game_week_team=game_week_team, position=player_in.position, starter=starter)
        else:
            GameWeekPlayer.objects.create(player=player_in, game_week_team=game_week_team, position=player_in.position, starter=False, benched_order=benched_order)

        starters = []
        benched_players = []

        for player in players:
            if player.starter:
                starters.append(player)
                continue
            benched_players.append(player)

        GameWeekTeam.objects.check_team_player_positions(players_starters=starters, players_benched=benched_players)

        player_transfer = PlayerTransfer(team=team, player_in=player_in, player_out=player_out, game_week=GAMEWEEK)
        player_transfer.save()

        return player_transfer

class PlayerTransfer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_in = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_transfer_player_in')
    player_out = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_transfer_player_out')
    game_week = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(38)])
    points_cost = models.IntegerField(default=0)

    objects = PlayerTransferManager()

    def save(self, *args, **kwargs) -> None:
        if self.team.bank - self.player_in.price + self.player_out.price < 0:
            raise ValidationError('player doesnt have enough money to make this transfer')
        if self.team.free_transfers == 0:
            self.points_cost = 4
        else:
            self.team.free_transfers -= 1

        return super().save(*args, **kwargs)


