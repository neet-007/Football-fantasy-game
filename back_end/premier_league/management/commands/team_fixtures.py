from django.core.management.base import BaseCommand

from web_scraping.league_table_and_fixtures import get_teams_fixtures
from premier_league.models import PremierLeagueTeamBase, TeamFixtures
from django.db import transaction
from pprint import pprint

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                teams_fixtures_list = get_teams_fixtures()
                teams_fixtures_objects_list = []
                base_teams_dict = { base_team.pk:base_team for base_team in PremierLeagueTeamBase.objects.all()}
                for item in teams_fixtures_list:
                    teams_fixtures_objects_list.append(TeamFixtures(
                        team = base_teams_dict[item.team],
                        date = item.date,
                        comp = item.comp,
                        game_week = item.game_week,
                        day = item.day,
                        ground = item.ground,
                        result = item.result,
                        goals_for = item.gf,
                        goals_against = item.ga,
                        opponent = base_teams_dict[item.opponent]
                    ))

                TeamFixtures.objects.bulk_create(teams_fixtures_objects_list)
        except Exception as e:
            print(e)