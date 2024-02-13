from django.core.management.base import BaseCommand

from web_scraping.league_table_and_fixtures import update_teams_fixtures
from premier_league.models import PremierLeagueTeamBase, TeamFixtures
from django.db import transaction

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                teams_fixtures_new_data = update_teams_fixtures()
                base_teams_dict = { base_team.pk:base_team for base_team in PremierLeagueTeamBase.objects.all()}
                teams_fixtures = TeamFixtures.objects.filter(result=None)
                teams_fixtures_to_update = []
                fields_to_update = ['date', 'comp', 'game_week', 'day', 'ground', 'result', 'goals_for', 'goals_against', 'opponent']
                for team_fixture in teams_fixtures:
                    team_fixture_new_data = teams_fixtures_new_data[f'{team_fixture.team.team_code}-{team_fixture.game_week}']
                    team_fixture.date = team_fixture_new_data.date
                    team_fixture.comp = team_fixture_new_data.comp
                    team_fixture.game_week = team_fixture_new_data.game_week
                    team_fixture.day = team_fixture_new_data.day
                    team_fixture.ground = team_fixture_new_data.ground
                    team_fixture.result = team_fixture_new_data.result
                    team_fixture.goals_for = team_fixture_new_data.gf
                    team_fixture.goals_against = team_fixture_new_data.ga
                    team_fixture.opponent = base_teams_dict[team_fixture_new_data.opponent]

                    teams_fixtures_to_update.append(team_fixture)

                TeamFixtures.objects.filter(result=None).bulk_update(teams_fixtures_to_update, fields_to_update)
        except Exception as e:
            print(f'{e} exception')
