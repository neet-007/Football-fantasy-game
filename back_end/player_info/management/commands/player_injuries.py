from django.core.management.base import BaseCommand

from django.db.transaction import atomic
from premier_league.models import PremierLeagueTeamBase
from player_info.models import Player, PlayerIjuriesAndBans
from web_scraping.player_injuries import get_injuries_and_suspensions

from traceback import print_exc


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        try:
            with atomic():
                injuries_and_suspensions_list = get_injuries_and_suspensions()
                record_to_create = []
                a = [player.player_first_name for player in injuries_and_suspensions_list]
                b = [player.player_last_name for player in injuries_and_suspensions_list]

                players_query = Player.objects.filter(first_name__in=a, last_name__in=b)
                players_query_b = Player.objects.filter(first_name__in=b, last_name__in=a)
                players_query_c = Player.objects.filter(last_name__in=b)
                players_query_d = Player.objects.filter(first_name__in=a)

                for player in players_query:
                    for p in injuries_and_suspensions_list:
                        if player.first_name == p.player_first_name and player.last_name == p.player_last_name:
                            record_to_create.append(PlayerIjuriesAndBans(player=player, first_name=p.player_first_name, last_name=p.player_last_name, status=p.player_injury_status, team=player.team, return_data=p.player_return_date))

                for player in players_query_b:
                    for p in injuries_and_suspensions_list:
                        if player.last_name == p.player_first_name and player.first_name == p.player_last_name:
                            record_to_create.append(PlayerIjuriesAndBans(player=player, first_name=p.player_first_name, last_name=p.player_last_name, status=p.player_injury_status, team=player.team, return_data=p.player_return_date))

                for player in players_query_c:
                    for p in injuries_and_suspensions_list:
                        if player.last_name == p.player_last_name and player.team.pk == p.player_team:
                            record_to_create.append(PlayerIjuriesAndBans(player=player, first_name=p.player_first_name, last_name=p.player_last_name, status=p.player_injury_status, team=player.team, return_data=p.player_return_date))

                for player in players_query_d:
                    for p in injuries_and_suspensions_list:
                        if player.first_name == p.player_first_name and player.team.pk == p.player_team:
                            record_to_create.append(PlayerIjuriesAndBans(player=player, first_name=p.player_first_name, last_name=p.player_last_name, status=p.player_injury_status, team=player.team, return_data=p.player_return_date))

                PlayerIjuriesAndBans.objects.bulk_create(record_to_create)
                """
                print(f'count:{len(injuries_and_suspensions_list)}')
                for player in injuries_and_suspensions_list:
                    print(f'{player.player_first_name}  {player.player_last_name}')
                """
        except:
            print_exc()