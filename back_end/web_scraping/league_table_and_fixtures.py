import requests
from bs4 import BeautifulSoup

LEAGUE_TABLE = 'https://fbref.com/en/comps/9/Premier-League-Stats'

def get_league_table():
    request = requests.get(LEAGUE_TABLE)
    soup = BeautifulSoup(request.content, 'html.parser')

    league_header = list(soup.find(name='table').find(name='thead').find(name='tr').findAll(name='th'))[:16]
    league_rows = list(soup.find(name='table').find(name='tbody').findAll(name='tr'))

    for i in range(len(league_rows)):
        team_dict = {}
        for j in range(len(league_header)):
            if j == 15:
                games = list(league_rows[i])[j].find(name='div').findAll(name='div')
                team_dict[league_header[j].text] = [div.find(name='a').text for div in games]
                continue
            team_dict[league_header[j].text] = list(league_rows[i])[j].text

        print(team_dict)