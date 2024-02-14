from django.core.management.base import BaseCommand

from traceback import print_exc

from django.db import transaction

from player_info.models import Player
from web_scraping.player_update_pricing import PlayerPricing


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        obj = PlayerPricing()
        players = Player.objects.all().order_by('team')
        new_data_dict = obj.get_teams_stats()
        player_to_update_list = []

        try:
            with transaction.atomic():
                clean_sheet = False
                for player in players:
                    game_week_points = 0
                    new_data_player = new_data_dict[f'{player.last_name} {player.team.team_code} {player.first_name}']

                    if player.position == 0:
                        clean_sheet = False
                        if 'CS' in new_data_player:
                            if new_data_player['CS'] > player.clean_sheets:
                                clean_sheet = True

                        if 'Saves' in new_data_player:
                            game_week_points += (new_data_player['Saves'] - player.saves) / 3

                    if clean_sheet and new_data_player['MP'] - player.matches_played > 60:
                        if player.position == 0 or player.position == 1:
                            game_week_points += 4
                        if player.position == 3:
                            game_week_points += 1

                    if new_data_player['Min']:
                        game_week_points += 1 if new_data_player['Min'] - player.minutes == 59 else 0
                        game_week_points += 2 if new_data_player['Min'] - player.minutes >=60 else 0

                    if new_data_player['Ast']:
                        game_week_points += 3 * (new_data_player['Ast'] - player.assists)

                    if new_data_player['CrdY']:
                        game_week_points -= 1 if new_data_player['CrdY'] - player.yellow_cards else 0

                    if new_data_player['CrdR']:
                        game_week_points -= 3 if new_data_player['CrdR'] - player.yellow_cards else 0

                    if new_data_player['PKatt'] and new_data_player['PK']:
                        if new_data_player['PKatt'] > player.penalties_attempted and new_data_player['PK'] == player.penalty_goals:
                            game_week_points -= 2

                    if new_data_player['Gls']:
                        if player.position == 0 or player.position == 1:
                            game_week_points += 6 * (new_data_player['Gls'] - player.goals)

                        if player.position == 3:
                            game_week_points += 5 * (new_data_player['Gls'] - player.goals)

                        if player.position == 4:
                            game_week_points += 3 * (new_data_player['Gls'] - player.goals)

                    player.matches_played = new_data_player['MP']
                    player.starts = new_data_player['Starts']
                    player.minutes = new_data_player['Min']
                    player.nineties = new_data_player['90s']
                    player.goals = new_data_player['Gls']
                    player.assists = new_data_player['Ast']
                    player.goals_and_assists = new_data_player['G+A']
                    player.none_penalty_goals = new_data_player['G-PK']
                    player.penalty_goals = new_data_player['PK']
                    player.penalties_attempted = new_data_player['PKatt']
                    player.yellow_cards = new_data_player['CrdY']
                    player.red_cards = new_data_player['CrdR']
                    player.game_week_points = game_week_points

                    player_to_update_list.append(player)


                Player.objects.bulk_update(player_to_update_list, ['matches_played', 'starts', 'minutes',
                                                                'nineties', 'goals', 'assists', 'goals_and_assists',
                                                                'none_penalty_goals', 'penalty_goals', 'penalties_attempted',
                                                                'yellow_cards', 'red_cards', 'game_week_points'])

                #make signal to change player game week game week points
                #GameWeekPlayer.objects.update(points=F('player__game_week_points'))
        except:
            print_exc()
