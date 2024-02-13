import requests
import pprint
from datetime import datetime
from bs4 import BeautifulSoup
from player_info.models import PlayerIjuriesAndBans
from utils.premier_league_utils import get_premier_league_team_int
from utils.player_info_utils import normalize_player_name

INJURIES_BASE_URL = 'https://www.fantasyfootballscout.co.uk/fantasy-football-injuries/'

def get_injuries_and_suspensions():
    request = requests.get(INJURIES_BASE_URL)
    soup = BeautifulSoup(request.content, 'html.parser')

    player_rows = soup.find(name='table').find(name='tbody').findAll(name='tr')
    for row in player_rows:
        player_dict = {}
        split_name =  row.contents[0].text.split(' ')
        player_dict['first_name'] = normalize_player_name(split_name[2])
        player_dict['last_name'] = normalize_player_name(split_name[3]) if len(split_name) > 3 else ''

        team_str = row.contents[1]['title'].lower()

        player_dict['team'] = get_premier_league_team_int(team=team_str)
        """
        if team_str == 'arsenal':
            player_dict['team'] = 0
        if team_str == 'aston villa':
            player_dict['team'] = 1
        if team_str == 'brentford':
            player_dict['team'] = 2
        if team_str == 'brighton and hove albion':
            player_dict['team'] = 3
        if team_str == 'bournemouth':
            player_dict['team'] = 4
        if team_str == 'burnley':
            player_dict['team'] = 5
        if team_str == 'chelsea':
            player_dict['team'] = 6
        if team_str == 'crystal palace':
            player_dict['team'] = 7
        if team_str == 'everton':
            player_dict['team'] = 8
        if team_str == 'fulham':
            player_dict['team'] = 9
        if team_str == 'liverpool':
            player_dict['team'] = 10
        if team_str == 'luton town':
            player_dict['team'] = 11
        if team_str == 'manchester city':
            player_dict['team'] = 12
        if team_str == 'manchester united':
            player_dict['team'] = 13
        if team_str == 'newcastle united':
            player_dict['team'] = 14
        if team_str == 'nottingham forest':
            player_dict['team'] = 15
        if team_str == 'sheffield united':
            player_dict['team'] = 16
        if team_str == 'tottenham hotspur':
            player_dict['team'] = 17
        if team_str == 'west ham united':
            player_dict['team'] = 18
        if team_str == 'wolverhampton wanderers':
            player_dict['team'] = 19
        """
        injury_status = row.contents[2].find(name='span')['class'][-1].split(' ')[-1].split('-')[-1].lower()
        if injury_status == '25':
            player_dict['status'] = 0
        if injury_status == '50':
            player_dict['status'] = 1
        if injury_status == '75':
            player_dict['status'] = 2
        if injury_status == 'injured':
            player_dict['status'] = 3
        if injury_status == 'suspended':
            player_dict['status'] = 4
        if row.contents[3].text.lower() == 'unknown':
            player_dict['return_data'] = None
        else:
            player_dict['return_data'] = datetime.strptime(row.contents[3].text, "%d/%m/%Y").date()
        if not 'team' in player_dict:
            raise ValueError(f'{ row.contents[1]['title']} is not registerd')
        PlayerIjuriesAndBans.objects.create(**player_dict)

    """
    for row in player_rows:
        buffer = []
        player_row = list(row)[:4]
        buffer.append(player_row[0].text)
        buffer.append(player_row[1].text)
        buffer.append(player_row[2].find(name='span')['class'])
        buffer.append(player_row[3].text)
        injuries_and_suspensions.append(buffer)
    """
