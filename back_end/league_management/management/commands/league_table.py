from django.core.management.base import BaseCommand

from web_scraping.league_table_and_fixtures import get_league_table
from premier_league.models import PremierLeagueTeam
from django.db import transaction

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                teams = get_league_table()
                teams_to_create = []
                for team in teams:
                    teams_to_create.append(PremierLeagueTeam(
                        name = team.name,
                        team_code = team.team_code,
                        postition = team.position,
                        matches_played = team.matches_played,
                        wins = team.wins,
                        losses = team.losses,
                        draws = team.draws,
                        goals_for = team.goals_for,
                        goals_against = team.goals_against,
                        goals_differance = team.goals_differance,
                        points = team.points,
                        points_per_match = team.points_per_match,
                        expected_goals_for = team.expected_goals_for,
                        expected_goals_against = team.expected_goals_againts,
                        expected_goals_differance = team.expected_goals_differance,
                        expected_goals_differance_per_ninety = team.expected_goals_differance_per_ninety,
                        last_five = team.last_five

                    ))

                PremierLeagueTeam.objects.bulk_create(teams_to_create)
        except Exception as e:
            print(e.with_traceback(e.__traceback__))