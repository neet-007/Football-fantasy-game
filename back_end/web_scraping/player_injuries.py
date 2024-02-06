import requests
import pprint
from datetime import datetime
from bs4 import BeautifulSoup
from player_info.models import PlayerIjuriesAndBans

INJURIES_BASE_URL = 'https://www.fantasyfootballscout.co.uk/fantasy-football-injuries/'

def get_injuries_and_suspensions():
    request = requests.get(INJURIES_BASE_URL)
    soup = BeautifulSoup(request.content, 'html.parser')

    player_rows = soup.find(name='table').find(name='tbody').findAll(name='tr')
    for row in player_rows:
        player_dict = {}
        player_dict['first_name'] =row.contents[0].text.split(' ')[2]
        player_dict['last_name'] = row.contents[0].text.split(' ')[3].replace('(','').replace(')','') if len(row.contents[0].text.split(' ')) > 3 else ''
        if row.contents[1]['title'].lower() == 'arsenal':
            player_dict['team'] = 0
        if row.contents[1]['title'].lower() == 'aston villa':
            player_dict['team'] = 1
        if row.contents[1]['title'].lower() == 'brentford':
            player_dict['team'] = 2
        if row.contents[1]['title'].lower() == 'brighton and hove albion':
            player_dict['team'] = 3
        if row.contents[1]['title'].lower() == 'bournemouth':
            player_dict['team'] = 4
        if row.contents[1]['title'].lower() == 'burnley':
            player_dict['team'] = 5
        if row.contents[1]['title'].lower() == 'chelsea':
            player_dict['team'] = 6
        if row.contents[1]['title'].lower() == 'crystal palace':
            player_dict['team'] = 7
        if row.contents[1]['title'].lower() == 'everton':
            player_dict['team'] = 8
        if row.contents[1]['title'].lower() == 'fulham':
            player_dict['team'] = 9
        if row.contents[1]['title'].lower() == 'liverpool':
            player_dict['team'] = 10
        if row.contents[1]['title'].lower() == 'luton town':
            player_dict['team'] = 11
        if row.contents[1]['title'].lower() == 'manchester city':
            player_dict['team'] = 12
        if row.contents[1]['title'].lower() == 'manchester united':
            player_dict['team'] = 13
        if row.contents[1]['title'].lower() == 'newcastle united':
            player_dict['team'] = 14
        if row.contents[1]['title'].lower() == 'nottingham forest':
            player_dict['team'] = 15
        if row.contents[1]['title'].lower() == 'sheffield united':
            player_dict['team'] = 16
        if row.contents[1]['title'].lower() == 'tottenham hotspur':
            player_dict['team'] = 17
        if row.contents[1]['title'].lower() == 'west ham united':
            player_dict['team'] = 18
        if row.contents[1]['title'].lower() == 'wolverhampton wanderers':
            player_dict['team'] = 19

        if row.contents[2].find(name='span')['class'][-1].split(' ')[-1].split('-')[-1].lower() == str(25):
            player_dict['status'] = 0
        if row.contents[2].find(name='span')['class'][-1].split(' ')[-1].split('-')[-1].lower() == str(50):
            player_dict['status'] = 1
        if row.contents[2].find(name='span')['class'][-1].split(' ')[-1].split('-')[-1].lower() == str(75):
            player_dict['status'] = 2
        if row.contents[2].find(name='span')['class'][-1].split(' ')[-1].split('-')[-1].lower() == 'injured':
            player_dict['status'] = 3
        if row.contents[2].find(name='span')['class'][-1].split(' ')[-1].split('-')[-1].lower() == 'suspended':
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
