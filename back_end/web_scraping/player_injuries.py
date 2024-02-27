import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils.premier_league_utils import get_verbose_premier_league_team_int
from utils.player_info_utils import split_name

INJURIES_BASE_URL = 'https://www.fantasyfootballscout.co.uk/fantasy-football-injuries/'

class PlayerInjuryAndSuspension():
    def __init__(self, data) -> None:
        self.data = data

    @property
    def player_first_name(self):
        if 'first_name' in self.data:
            return self.data['first_name']
        return None

    @property
    def player_last_name(self):
        if 'last_name' in self.data:
            return self.data['last_name']
        return None

    @property
    def player_team(self):
        return self.data['team']

    @property
    def player_injury_status(self):
        return self.data['status']

    @property
    def player_return_date(self):
        return self.data['return_date']

def get_injuries_and_suspensions() -> list[PlayerInjuryAndSuspension]:
    injuries_and_suspensions_list = []
    try:
        request = requests.get(INJURIES_BASE_URL)
        request.raise_for_status()

        soup = BeautifulSoup(request.content, 'html.parser')

        player_rows = soup.find(name='table').find(name='tbody').findAll(name='tr')
        for row in player_rows:
            player_dict = {}
            name_dict =  split_name(row.contents[0].text, injuries=True)
            player_dict['first_name'] = name_dict['first_name']
            player_dict['last_name'] = name_dict['last_name']

            player_dict['team'] = get_verbose_premier_league_team_int(team=row.contents[1]['title'].lower())

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
                player_dict['return_date'] = None
            else:
                player_dict['return_date'] = datetime.strptime(row.contents[3].text, "%d/%m/%Y").date()
            if not 'team' in player_dict:
                raise ValueError(f'{ row.contents[1]['title']} is not registerd')

            injuries_and_suspensions_list.append(PlayerInjuryAndSuspension(data=player_dict))

    except Exception as e:
        print(e)

    return injuries_and_suspensions_list