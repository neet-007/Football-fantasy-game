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

GAME_WEEK = 1

class PlayerPricing():
    def __init__(self) -> None:
        self.teams_urls = get_teams_urls()

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

                            if s_name['first_name'] == player_dict['first_name'] and s_name['last_name'] == player_dict['last_name']:
                                print(f'gk match {player_dict["first_name"]} {player_dict["last_name"]}')
                                player_dict[keeper_headers[11].text] = keeper_row[11].text
                                player_dict[keeper_headers[16].text] = keeper_row[16].text
                                player_dict[keeper_headers[19].text] = keeper_row[19].text

                    players_dict[f'{player_dict['last_name']} {player_dict['Team']} {player_dict['first_name']}'] = player_dict

            except Exception as e:
                raise ValueError(f'{player_dict['first_name']} {team} {e}')


        return players_dict
