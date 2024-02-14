from django.core.management.base import BaseCommand

from premier_league.models import PremierLeagueTeamBase
from player_info.models import Player
from django.db import transaction, IntegrityError
from web_scraping.player_stats import GetPlayerStats


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        base_teams_dict = {base_team.team_code:base_team for base_team in PremierLeagueTeamBase.objects.all()}
        player_objects = GetPlayerStats().get_player_stats()
        try:
            with transaction.atomic():
                players_list_to_create = [
                    Player(
                        first_name = player.player_first_name,
                        last_name = player.player_last_name,
                        nation = player.player_nation,
                        position = player.player_postition,
                        age = player.player_age,
                        matches_played = player.player_matches_played,
                        starts = player.player_starts,
                        minutes = player.player_minutes_played,
                        nineties = player.player_90s,
                        goals = player.player_goals,
                        assists = player.player_assists,
                        goals_and_assists = player.player_goals_and_assists,
                        none_penalty_goals = player.player_non_penalty_goals,
                        penalty_goals = player.player_penalty_goals,
                        penalties_attempted = player.player_penalties_attempted,
                        yellow_cards = player.player_yellow_cards,
                        red_cards = player.player_red_cards,
                        team = base_teams_dict[player.player_team],
                        saves = player.player_saves,
                        penalty_saves = player.player_penalty_saves,
                        clean_sheets = player.player_clean_sheets,
                    )
                for player in player_objects]

                Player.objects.bulk_create(players_list_to_create)

        except Exception as e:
            print(e)
