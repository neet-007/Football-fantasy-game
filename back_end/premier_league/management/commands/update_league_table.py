from django.core.management.base import BaseCommand

from web_scraping.league_table_and_fixtures import update_league_table
from premier_league.models import PremierLeagueTeam
from django.db import transaction

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                teams_new_data = update_league_table()
                teams = PremierLeagueTeam.objects.all()
                teams_to_update = []
                fields_to_update = ['postition', 'matches_played', 'wins', 'losses', 'draws', 'goals_for', 'goals_against', 'goals_differance', 'points', 'points_per_match', 'expected_goals_for', 'expected_goals_against', 'expected_goals_differance', 'expected_goals_differance_per_ninety', 'last_five']
                for team in teams:
                    team_new_data = teams_new_data[team.base_team.pk]

                    team.postition = team_new_data.position
                    team.matches_played = team_new_data.matches_played
                    team.wins = team_new_data.wins
                    team.losses = team_new_data.losses
                    team.draws = team_new_data.draws
                    team.goals_for = team_new_data.goals_for
                    team.goals_against = team_new_data.goals_against
                    team.goals_differance = team_new_data.goals_differance
                    team.points = team_new_data.points
                    team.points_per_match = team_new_data.points_per_match
                    team.expected_goals_for = team_new_data.expected_goals_for
                    team.expected_goals_against = team_new_data.expected_goals_againts
                    team.expected_goals_differance = team_new_data.expected_goals_differance
                    team.expected_goals_differance_per_ninety = team_new_data.expected_goals_differance_per_ninety
                    team.last_five = team_new_data.last_five

                    teams_to_update.append(team)

                PremierLeagueTeam.objects.bulk_update(teams_to_update, fields_to_update)
        except Exception as e:
            print(e)
