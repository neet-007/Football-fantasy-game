import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint
from .player_stats import get_teams_urls

LEAGUE_TABLE = 'https://fbref.com/en/comps/9/Premier-League-Stats'

class PremierLeagueTeam():
    def __init__(self, data) -> None:
        self.data = data

    @property
    def name(self):
        return self.data['Squad'].lower()

    @property
    def team_code(self):
        if self.name == 'arsenal':
            return 0
        if self.name == 'aston villa':
            return 1
        if self.name == 'brentford':
            return 2
        if self.name == 'brighton':
            return 3
        if self.name == 'bournemouth':
            return 4
        if self.name == 'burnley':
            return 5
        if self.name == 'chelsea':
            return 6
        if self.name == 'crystal palace':
            return 7
        if self.name == 'everton':
            return 8
        if self.name == 'fulham':
            return 9
        if self.name == 'liverpool':
            return 10
        if self.name == 'luton town':
            return 11
        if self.name == 'manchester city':
            return 12
        if self.name == 'manchester utd':
            return 13
        if self.name == 'newcastle utd':
            return 14
        if self.name == "nott'ham forest":
            return 15
        if self.name == 'sheffield utd':
            return 16
        if self.name == 'tottenham':
            return 17
        if self.name == 'west ham':
            return 18
        if self.name == 'wolves':
            return 19
        raise ValueError(f'{self.name} is not registerd')

    @property
    def position(self):
        return int(self.data['Rk'])

    @property
    def matches_played(self):
        return int(self.data['MP'])

    @property
    def wins(self):
        return int(self.data['W'])

    @property
    def losses(self):
        return int(self.data['L'])

    @property
    def draws(self):
        return int(self.data['D'])

    @property
    def goals_for(self):
        return int(self.data['GF'])

    @property
    def goals_against(self):
        return int(self.data['GA'])

    @property
    def goals_differance(self):
        return float(self.data['GD'])

    @property
    def points(self):
        return int(self.data['Pts'])

    @property
    def points_per_match(self):
        return float(self.data['Pts/MP'])

    @property
    def expected_goals_for(self):
        return float(self.data['xG'])

    @property
    def expected_goals_againts(self):
        return float(self.data['xGA'])

    @property
    def expected_goals_differance(self):
        return float(self.data['xGD'])

    @property
    def expected_goals_differance_per_ninety(self):
        return float(self.data['xGD/90'])

    @property
    def last_five(self):
        return ' '.join(self.data['Last 5'])

class TeamFixture():
    def __init__(self, data) -> None:
        self.data = data

    def get_team_int(self, team:str) -> int:
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

    def get_ground_int(self, ground:str) -> int:
        if ground == 'home':
            return 0
        if ground == 'away':
            return 1

    def get_day_int(self, day:str) -> int:
        if day == 'sat':
            return 0
        if day == 'sun':
            return 1
        if day == 'mon':
            return 2
        if day == 'tue':
            return 3
        if day == 'wed':
            return 4
        if day == 'thu':
            return 5
        if day == 'fri':
            return 6

    def get_result_int(self, result:str) -> int:
        if result == 'w':
            return 0
        if result == 'l':
            return 1
        if result == 'd':
            return 2

    @property
    def team(self):
        return self.get_team_int(self.data['team'])

    @property
    def date(self):
        return datetime.strptime(self.data['date'], '%Y-%m-%d').date()

    @property
    def comp(self):
        if self.data['comp'].lower() == 'premier league':
            return 0

    @property
    def game_week(self):
        return self.data['game_week'].lower().replace('matchweek ','')

    @property
    def day(self):
        return self.get_day_int(self.data['day'].lower())

    @property
    def ground(self):
        return self.get_ground_int(self.data['ground'].lower())

    @property
    def result(self):
        return self.get_result_int(self.data['result'].lower())

    @property
    def gf(self):
        return int(self.data['gf']) if self.data['gf'] != '' else None

    @property
    def ga(self):
        return int(self.data['ga']) if self.data['gf'] != '' else None

    @property
    def opponent(self):
        return self.get_team_int(self.data['opponent'].lower())

def get_league_table():
    request = requests.get(LEAGUE_TABLE)
    soup = BeautifulSoup(request.content, 'html.parser')

    league_header = list(soup.find(name='table').find(name='thead').find(name='tr').findAll(name='th'))[:16]
    league_rows = list(soup.find(name='table').find(name='tbody').findAll(name='tr'))

    teams_list = []
    for i in range(len(league_rows)):
        team_dict = {}
        for j in range(len(league_header)):
            if j == 15:
                games = list(league_rows[i])[j].find(name='div').findAll(name='div')
                team_dict[league_header[j].text] = [div.find(name='a').text for div in games]
                continue
            team_dict[league_header[j].text] = list(league_rows[i])[j].text

        teams_list.append(PremierLeagueTeam(data=team_dict))

    for item in teams_list:
        print(item.name)
        print(item.team_code)
        print(item.last_five)
        print(item.points)

def get_teams_fixtures() -> list:
    try:
        teams_urls = get_teams_urls()
        teams_fixtures_list = []
        for team, url in teams_urls.items():
            request = requests.get(url=url)
            request.raise_for_status()
            soup = BeautifulSoup(request.content, 'html.parser')
            fixtures_table = list(soup.find(attrs={'id':'matchlogs_for'}).find(name='tbody').findAll(name='tr'))

            for tr in fixtures_table:
                fixture_dict = {}
                tr_list = list(tr.findAll(name='td'))[1:9]
                if tr_list[0].text.lower() != 'premier league':
                    continue

                fixture_dict['team'] = team
                fixture_dict['date'] = tr.find(name='th').text
                fixture_dict['comp'] = tr_list[0].text
                fixture_dict['game_week'] = tr_list[1].text
                fixture_dict['day'] = tr_list[2].text
                fixture_dict['ground'] = tr_list[3].text
                fixture_dict['result'] = tr_list[4].text
                fixture_dict['gf'] = tr_list[5].text
                fixture_dict['ga'] = tr_list[6].text
                fixture_dict['opponent'] = tr_list[7].text

                teams_fixtures_list.append(TeamFixture(data=fixture_dict))

        return teams_fixtures_list
    except Exception as e:
        print(e)
#matchlogs_for