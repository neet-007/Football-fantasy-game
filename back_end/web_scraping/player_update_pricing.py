from .player_stats import get_teams_urls
from player_info.models import Player
from team_management.models import GameWeekPlayer
from django.db import transaction
import requests
from bs4 import BeautifulSoup
from player_info.models import Player
from decimal import Decimal
from django.db.models import F

from utils.premier_league_utils import get_premier_league_team_int
from utils.player_info_utils import split_name

import unicodedata
import re

GAME_WEEK = 1

def normalize_name(name):
    if not name:
        return None
    # Normalize to NFKD Unicode form to separate diacritics
    normalized_name = unicodedata.normalize('NFKD', name)
    # Remove any character that is not a letter, digit, or whitespace
    normalized_name = re.sub(r'[^\w\s]', '', normalized_name)
    # Convert to lowercase
    normalized_name = normalized_name.lower()
    # Remove leading and trailing whitespaces
    normalized_name = normalized_name.strip()
    return normalized_name
class PlayerPricing():
    def __init__(self) -> None:
        self.teams_urls = get_teams_urls()
    """
    def get_team_int(self, name:str, team:str) -> int:
        if team == 'arsenal':
            return 0
        if team == 'aston villa':
            return 1
        if team == 'brentford':
            return 2
        if team == 'brighton':
            return 3
        if team == 'bournemouth':
            return 4
        if team == 'burnley':
            return 5
        if team == 'chelsea':
            return 6
        if team == 'crystal palace':
            return 7
        if team == 'everton':
            return 8
        if team == 'fulham':
            return 9
        if team == 'liverpool':
            return 10
        if team == 'luton town':
            return 11
        if team == 'manchester city':
            return 12
        if team == 'manchester utd':
            return 13
        if team == 'newcastle utd':
            return 14
        if team == "nott'ham forest":
            return 15
        if team == 'sheffield utd':
            return 16
        if team == 'tottenham':
            return 17
        if team == 'west ham':
            return 18
        if team == 'wolves':
            return 19
        raise ValueError(f'{name} {team} is not registerd')
    """

    def get_position_int(self, name:str, position:str) -> int:
        if ',' in position:
            position = position.split(',')[0]
        if position == 'GK':
            return 0
        if position == 'DF':
            return 1
        if position == 'MF':
            return 3
        if position == 'FW':
            return 4
        else:
            raise ValueError(f'{name} {position}')

    def get_teams_stats(self) -> dict[str, dict]:
        players_dict = {}
        for team, url in  self.teams_urls.items():
            request = requests.get(url)
            soup = BeautifulSoup(request.content, 'html.parser')
            player_headers =  soup.find(attrs={'id':'stats_standard_9'}).findAll(name='tr')[1].findAll('th')
            player_rows = soup.find(attrs={'id':'stats_standard_9'}).find(name='tbody').findAll(name='tr')
            keeper_headers = list(soup.find(attrs={'id':'stats_keeper_9'}).findAll(name='tr')[1].findAll(name='th'))
            keepers_rows = soup.find(attrs={'id':'stats_keeper_9'}).find(name='tbody').findAll(name='tr')

            try:
                for row in player_rows:
                    player_dict = {}
                    player_row = list(row)
                    s_name = split_name(player_row[0].find(name='a').text)
                    player_dict['first_name'] = s_name['first_name']
                    player_dict['last_name'] = s_name['last_name']

                    """
                    player_dict['first_name'] = normalize_name(split_name[0])
                    player_dict['middle_name'] = normalize_name(split_name[1]) if len(split_name) > 2 else None
                    if len(split_name) == 2:
                        player_dict['last_name'] = normalize_name(split_name[1])
                    elif len(split_name) > 2:
                        player_dict['last_name'] = normalize_name(split_name[2])
                    else:
                        player_dict['last_name'] = None
                    """
                    player_dict['Team'] = get_premier_league_team_int(team)

                    for header, td in zip(player_headers[2:16], player_row[2:16]):
                        if td.text == None or td.text == '':
                            player_dict[header.text] = None
                        elif header.text == 'Age':
                            pass
                        elif header.text == 'Pos':
                            player_dict[header.text] = self.get_position_int(player_dict['first_name'], td.text)
                        elif header.text == '90s':
                            player_dict[header.text] = Decimal(td.text)
                        elif header.text == 'Min':
                            player_dict[header.text] = int(td.text.replace(',', ''))
                        else:
                            player_dict[header.text] =  int(td.text)

                    if player_dict['Pos'] == 'GK':
                        print(f'gk found {player_dict['first_name']} {player_dict["last_name"]}')
                        for row in keepers_rows:
                            keeper_row = list(row)
                            s_name = split_name(keeper_row[0].find(name='a').text)
                            """
                            keeper_dict['first_name'] = split_name[0]
                            keeper_dict['middle_name'] = split_name[1] if len(split_name) > 2 else None
                            if len(split_name) == 2:
                                keeper_dict['last_name'] = (split_name[1])
                            elif len(split_name) > 2:
                                keeper_dict['last_name'] = (split_name[2])
                            else:
                                keeper_dict['last_name'] = None
                            """
                            if s_name['first_name'] == player_dict['first_name'] and s_name['last_name'] == player_dict['last_name']:
                                print(f'gk match {player_dict["first_name"]} {player_dict["last_name"]}')
                                player_dict[keeper_headers[11].text] = keeper_row[11].text
                                player_dict[keeper_headers[16].text] = keeper_row[16].text
                                player_dict[keeper_headers[19].text] = keeper_row[19].text

                    players_dict[f'{player_dict['last_name']} {player_dict['Team']} {player_dict['first_name']}'] = player_dict

            except Exception as e:
                raise ValueError(f'{player_dict['first_name']} {team} {e}')


        return players_dict

    def player_update_and_pricing(self) -> None:
        players = Player.objects.all().order_by('team')
        new_data_dict = self.get_teams_stats()
        player_to_update_list = []
        try:
            with transaction.atomic():
                clean_sheet = False
                for player in players:
                    game_week_points = 0
                    new_data_player = new_data_dict[f'{player.last_name} {player.team} {player.first_name}']

                    if player.position == 0:
                        clean_sheet = False
                        if new_data_player['CS'] > player.clean_sheets:
                            clean_sheet = True

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
        except Exception as e:
            print(e)