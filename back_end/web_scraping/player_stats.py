import requests
import pprint
from bs4 import BeautifulSoup
from player_info.models import Player
from decimal import Decimal
from django.db import transaction, IntegrityError

TEAM_STATS_BASE_URL = 'https://fbref.com/'

def get_teams_urls():
    request = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats')
    soup = BeautifulSoup(request.content, 'html.parser')

    team_rows = soup.find(attrs={'id':'results2023-202491_overall'}).find(name='tbody').find_all(name='tr')
    teams_urls = {(tr.find(name='td').find(name='a').text).lower():TEAM_STATS_BASE_URL + tr.find(name='td').find(name='a')['href'] for tr in team_rows}

    return teams_urls

def get_teams_stats(team, url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    player_rows = soup.find(attrs={'id':'stats_standard_9'}).find(name='tbody').findAll(name='tr')

    team_dict = {team:[]}
    for row in player_rows:
        player_list = []
        player_dict = {}
        player_row = list(row)
        player_list.append(player_row[0].find(name='a').text)
        player_list.append(player_row[1].find(name='a').find(name='span').text.split(' ')[-1])
        for td in player_row[2:]:
            player_list.append(td.text)
        player_dict[player_row[0].find(name='a').text] = player_list
        team_dict[team].append(player_dict)

    return team_dict
    #stats_standard_9

class PlayerStats:
    def __init__(self, data) -> None:
        self.data = data
    
    @property
    def player_first_name(self):
        if 'first_name' in self.data:
            return self.data['first_name']

    @property
    def player_last_name(self):
        if 'last_name' in self.data:
            return self.data['last_name']

    @property
    def player_nation(self):
        if 'Nation' in self.data:
            return self.data['Nation']

    @property
    def player_postition(self):
        if ',' in self.data['Pos']:
            self.data['Pos'] = self.data['Pos'].split(',')[0]
        if self.data['Pos'] == 'GK':
            return 0
        if self.data['Pos'] == 'DF':
            return 1
        if self.data['Pos'] == 'MF':
            return 3
        if self.data['Pos'] == 'FW':
            return 4
        else:
            raise ValueError(f'{self.data['first_name']} {self.data['Pos']}')

    @property
    def player_age(self):
        return self.data['Age']

    @property
    def player_matches_played(self):
        return self.data['MP']

    @property
    def player_starts(self):
        return self.data['Starts']

    @property
    def player_minutes_played(self):
        if 'Min' in self.data:
            return self.data['Min']

    @property
    def player_90s(self):
        if '90s' in self.data:
            return self.data['90s']

    @property
    def player_goals(self):
        if 'Gls' in self.data:
            try:
                return self.data['Gls']
            except Exception as e:
                raise ValueError(f'{self.data['first_name']}')

    @property
    def player_assists(self):
        if 'Ast' in self.data:
            return self.data['Ast']

    @property
    def player_goals_and_assists(self):
        if 'G+A' in self.data:
            return self.data['G+A']

    @property
    def player_non_penalty_goals(self):
        if 'G-PK' in self.data:
            return self.data['G-PK']

    @property
    def player_penalty_goals(self):
        if 'PK' in self.data:
            return self.data['PK']

    @property
    def player_penalties_attempted(self):
        if 'PKatt' in self.data:
            return self.data['PKatt']

    @property
    def player_yellow_cards(self):
        if 'CrdY' in self.data:
            return self.data['CrdY']

    @property
    def player_red_cards(self):
        if 'CrdR' in self.data:
            return self.data['CrdR']

    @property
    def player_team(self):
        if self.data['Team'] == 'arsenal':
            return 0
        if self.data['Team'] == 'aston villa':
            return 1
        if self.data['Team'] == 'brentford':
            return 2
        if self.data['Team'] == 'brighton and hove albion':
            return 3
        if self.data['Team'] == 'bournemouth':
            return 4
        if self.data['Team'] == 'burnley':
            return 5
        if self.data['Team'] == 'chelsea':
            return 6
        if self.data['Team'] == 'crystal palace':
            return 7
        if self.data['Team'] == 'everton':
            return 8
        if self.data['Team'] == 'fulham':
            return 9
        if self.data['Team'] == 'liverpool':
            return 10
        if self.data['Team'] == 'luton town':
            return 11
        if self.data['Team'] == 'manchester city':
            return 12
        if self.data['Team'] == 'manchester united':
            return 13
        if self.data['Team'] == 'newcastle united':
            return 14
        if self.data['Team'] == 'nottingham forest':
            return 15
        if self.data['Team'] == 'sheffield united':
            return 16
        if self.data['Team'] == 'tottenham hotspur':
            return 17
        if self.data['Team'] == 'west ham united':
            return 18
        if self.data['Team'] == 'wolverhampton wanderers':
            return 19
        raise ValueError(f'{self.data['Team']} is not registerd')

class GetPlayerStats:
    def __init__(self) -> None:
        pass

    def get_teams_urls(self):
        request = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats')
        request.raise_for_status()
        soup = BeautifulSoup(request.content, 'html.parser')

        team_rows = soup.find(attrs={'id':'results2023-202491_overall'}).find(name='tbody').find_all(name='tr')
        #teams_urls = {(tr.find(name='td').find(name='a').text).lower():TEAM_STATS_BASE_URL + tr.find(name='td').find(name='a')['href'] for tr in team_rows}
        teams_urls = {}
        for tr in team_rows:
            teams_urls[tr.find(name='td').find(name='a')['href'].split('/')[-1].lower().replace('-stats', '').lower().replace('-',' ')] = TEAM_STATS_BASE_URL + tr.find(name='td').find(name='a')['href']


        return teams_urls

    def get_teams_players_stats(self, team, url, i):
        request = requests.get(url)
        soup = BeautifulSoup(request.content, 'html.parser')
        player_headers =  soup.find(attrs={'id':'stats_standard_9'}).findAll(name='tr')[1].findAll('th')
        player_rows = soup.find(attrs={'id':'stats_standard_9'}).find(name='tbody').findAll(name='tr')

        try:
            for row in player_rows:
                player_dict = {}
                player_row = list(row)
                split_name = player_row[0].find(name='a').text.split(' ')
                player_dict['first_name'] = split_name[0]
                player_dict['last_name'] = ' '.join(split_name[1:]) if len(split_name) > 1 else ''
                try:
                    player_dict['Nation'] = player_row[1].find(name='a').find(name='span').text.split(' ')[-1]
                except:
                    pass
                player_dict['Team'] = team
                for header, td in zip(player_headers[2:16], player_row[2:16]):
                    if td.text == None or td.text == '':
                        player_dict[header.text] = None
                    elif header.text == 'Age':
                        player_dict[header.text] = int(td.text.split('-')[0])
                    elif header.text == 'Pos':
                        player_dict[header.text] = td.text
                    elif header.text == '90s':
                        player_dict[header.text] = Decimal(td.text)
                    elif header.text == 'Min':
                        player_dict[header.text] = int(td.text.replace(',', ''))
                    else:
                        player_dict[header.text] =  int(td.text)

                player_object = PlayerStats(data=player_dict)
                try:
                    with transaction.atomic():
                        Player.objects.create(
                            first_name= player_object.player_first_name,
                            last_name= player_object.player_last_name,
                            nation=player_object.player_nation,
                            age = player_object.player_age,
                            position= player_object.player_postition,
                            matches_played = player_object.player_matches_played,
                            starts = player_object.player_starts,
                            minutes = player_object.player_minutes_played,
                            nineties = player_object.player_90s,
                            goals = player_object.player_goals,
                            assists = player_object.player_assists,
                            goals_and_assists = player_object.player_goals_and_assists,
                            none_penalty_goals = player_object.player_non_penalty_goals,
                            penalty_goals = player_object.player_penalty_goals,
                            penalties_attempted = player_object.player_penalties_attempted,
                            yellow_cards = player_object.player_yellow_cards,
                            red_cards = player_object.player_red_cards,
                            team=player_object.player_team
                        )
                except IntegrityError:
                    raise ValueError(f'{player_dict["first_name"]} {team} {i}')

        except:
            raise ValueError(f'{player_dict['first_name']} {header.text} {team} {i}')


    def get_player_stats(self):
        team_urls = self.get_teams_urls()
        i = 0
        for key, value in team_urls.items():
            i += 1
            self.get_teams_players_stats(team=key, url=value, i=i)

    def test(self):
        team_urls = self.get_teams_urls()
        return self.get_teams_players_stats(team='liverpool', url=team_urls['liverpool'])




