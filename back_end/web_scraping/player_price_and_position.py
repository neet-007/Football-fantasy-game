from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

from utils.premier_league_utils import get_extreme_abbrieviated_preimer_league_team_int
from utils.player_info_utils import split_name

import unicodedata
import re


FPL_WEBSITE = 'https://fantasy.premierleague.com/player-list'
"""
def normalize_name(name):
    if name == None:
        return None
    print(f'in {name}')
    # Normalize to NFKD Unicode form to separate diacritics
    normalized_name = unicodedata.normalize('NFKD', name)
    # Remove any character that is not a letter, digit, or whitespace
    normalized_name = re.sub(r'[^\w\s]', '', normalized_name)
    # Convert to lowercase
    normalized_name = normalized_name.lower()
    # Remove leading and trailing whitespaces
    normalized_name = normalized_name.strip()
    print(f'out {normalized_name}')
    return normalized_name
"""

"""
def get_long_part(str:str) -> str:
    str = str.lower()
    if not '.' in str:
        return str
    str = str.split('.')
    if len(str[0]) > len(str[1]) and len(str[0]) > 1:
        return str[0]
    if len(str[1]) > 1:
        return str[1]
    return None
"""

def get_fpl_data() -> dict[str, dict]:
    driver = webdriver.Chrome()
    driver.get(url=FPL_WEBSITE)

    players_position_dict = {}
    first_last_dict = {}
    last_dict = {}
    first_dict = {}
    try:
        sleep(40)
        containers = driver.find_elements(By.CLASS_NAME, 'Layout__Main-eg6k6r-1')
        for container in containers:
            header = container.find_element(By.TAG_NAME, 'h3').text.lower()

            tables = container.find_elements(By.TAG_NAME, 'tbody')
            for table in tables:
                table_row = table.find_elements(By.TAG_NAME, 'tr')
                for tr in table_row:
                    player_dict = {}
                    player_row = tr.find_elements(By.TAG_NAME, 'td')
                    for i in range(len(player_row)):
                        if i == 0:
                            name = split_name(player_row[i].text)
                            player_dict['first_name'] = name['first_name']
                            player_dict['last_name'] = name['last_name']
                            """
                            name_length = len(name)
                            #get_long_part = lambda name_str: max(name_str.split('.'), key=lambda x: len(x)) if len(name_str.split('.')) >= 2 else None
                            if name_length == 1:
                                player_dict['first_name'] = None
                                player_dict['middle_name'] = None
                                player_dict['last_name'] = normalize_name(get_long_part(name[0]))
                            if name_length == 2:
                                player_dict['first_name'] = normalize_name(get_long_part(name[0]))
                                player_dict['middle_name'] = None
                                player_dict['last_name'] = normalize_name(get_long_part(name[1]))
                            if name_length == 3:
                                player_dict['first_name'] = normalize_name(get_long_part(name[0]))
                                player_dict['middle_name'] = normalize_name(get_long_part(name[1]))
                                player_dict['last_name'] = normalize_name(get_long_part(name[2]))
                            """
                        if i == 1:
                            #player_dict['team'] = player_row[i].text.lower()
                            player_dict['team'] = get_extreme_abbrieviated_preimer_league_team_int(player_row[i].text.lower())
                            """
                            if player_row[i].text.lower() == 'arsenal':
                                player_dict['team'] = 0
                            elif player_row[i].text.lower() == 'aston villa':
                                player_dict['team'] = 1
                            elif player_row[i].text.lower() == 'brentford':
                                player_dict['team'] = 2
                            elif player_row[i].text.lower() == 'brighton':
                                player_dict['team'] = 3
                            elif player_row[i].text.lower() == 'bournemouth':
                                player_dict['team'] = 4
                            elif player_row[i].text.lower() == 'burnley':
                                player_dict['team'] = 5
                            elif player_row[i].text.lower() == 'chelsea':
                                player_dict['team'] = 6
                            elif player_row[i].text.lower() == 'crystal palace':
                                player_dict['team'] = 7
                            elif player_row[i].text.lower() == 'everton':
                                player_dict['team'] = 8
                            elif player_row[i].text.lower() == 'fulham':
                                player_dict['team'] = 9
                            elif player_row[i].text.lower() == 'liverpool':
                                player_dict['team'] = 10
                            elif player_row[i].text.lower() == 'luton':
                                player_dict['team'] = 11
                            elif player_row[i].text.lower() == 'man city':
                                player_dict['team'] = 12
                            elif player_row[i].text.lower() == 'man utd':
                                player_dict['team'] = 13
                            elif player_row[i].text.lower() == 'newcastle':
                                player_dict['team'] = 14
                            elif player_row[i].text.lower() == "nott'm forest":
                                player_dict['team'] = 15
                            elif player_row[i].text.lower() == 'sheffield utd':
                                player_dict['team'] = 16
                            elif player_row[i].text.lower() == 'spurs':
                                player_dict['team'] = 17
                            elif player_row[i].text.lower() == 'west ham':
                                player_dict['team'] = 18
                            elif player_row[i].text.lower() == 'wolves':
                                player_dict['team'] = 19
                            else:
                                raise ValueError(f'{player_row[i].text.lower()} is not registerd')
                            """
                        if i == 2:
                            continue
                        player_dict['price'] = player_row[i].text.replace('£','').lower()
                        if header == 'goalkeepers':
                            player_dict['pos'] = 0
                        elif header == 'defenders':
                            player_dict['pos'] = 1
                        elif header == 'midfielders':
                            player_dict['pos'] = 3
                        elif header == 'forwards':
                            player_dict['pos'] = 4
                        else:
                            raise ValueError('position is not registerd')
                    if player_dict['first_name']:
                        if not player_dict['last_name']:
                            first_dict[f'{player_dict["first_name"]}-{player_dict["team"]}'] = player_dict
                        else:
                            first_last_dict[f'{player_dict["first_name"]}-{player_dict["last_name"]}-{player_dict["team"]}'] = player_dict
                    else:
                        last_dict[f'{player_dict['last_name']}-{player_dict['team']}'] = player_dict
        #pprint(players_position_dict)
        #print(sorted(set(d['team'] for d in players_position_dict.values())))
        #header = driver.find_element(By.CLASS_NAME, 'Layout__Main-eg6k6r-1').find_element(By.TAG_NAME, 'h3')
        #print(header.text)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        players_position_dict['first_last_dict'] = first_last_dict
        players_position_dict['last_dict'] = last_dict
        players_position_dict['first_dict'] = first_dict
        return players_position_dict
    """
    request = requests.get(url=FPL_WEBSITE)
    soup = BeautifulSoup(request.content, 'html.parser')

    players_tables = soup.find('div', {'id':'root'}).find_all('div')
    print(players_tables)
    """

def get_fpl_data_one_dict() -> dict[str, dict]:
    driver = webdriver.Chrome()
    driver.get(url=FPL_WEBSITE)

    players_position_dict = {}
    try:
        sleep(40)
        containers = driver.find_elements(By.CLASS_NAME, 'Layout__Main-eg6k6r-1')
        for container in containers:
            header = container.find_element(By.TAG_NAME, 'h3').text.lower()

            tables = container.find_elements(By.TAG_NAME, 'tbody')
            for table in tables:
                table_row = table.find_elements(By.TAG_NAME, 'tr')
                for tr in table_row:
                    player_dict = {}
                    player_row = tr.find_elements(By.TAG_NAME, 'td')
                    for i in range(len(player_row)):
                        if i == 0:
                            name = split_name(player_row[i].text)
                            player_dict['first_name'] = name['first_name']
                            player_dict['last_name'] = name['last_name']
                            """
                            name_length = len(name)
                            #get_long_part = lambda name_str: max(name_str.split('.'), key=lambda x: len(x)) if len(name_str.split('.')) >= 2 else None
                            if name_length == 1:
                                player_dict['first_name'] = None
                                player_dict['middle_name'] = None
                                player_dict['last_name'] = normalize_name(get_long_part(name[0]))
                            if name_length == 2:
                                player_dict['first_name'] = normalize_name(get_long_part(name[0]))
                                player_dict['middle_name'] = None
                                player_dict['last_name'] = normalize_name(get_long_part(name[1]))
                            if name_length == 3:
                                player_dict['first_name'] = normalize_name(get_long_part(name[0]))
                                player_dict['middle_name'] = normalize_name(get_long_part(name[1]))
                                player_dict['last_name'] = normalize_name(get_long_part(name[2]))
                            """
                        if i == 1:
                            #player_dict['team'] = player_row[i].text.lower()
                            player_dict['team'] = get_extreme_abbrieviated_preimer_league_team_int(player_row[i].text.lower())
                            """
                            if player_row[i].text.lower() == 'arsenal':
                                player_dict['team'] = 0
                            elif player_row[i].text.lower() == 'aston villa':
                                player_dict['team'] = 1
                            elif player_row[i].text.lower() == 'brentford':
                                player_dict['team'] = 2
                            elif player_row[i].text.lower() == 'brighton':
                                player_dict['team'] = 3
                            elif player_row[i].text.lower() == 'bournemouth':
                                player_dict['team'] = 4
                            elif player_row[i].text.lower() == 'burnley':
                                player_dict['team'] = 5
                            elif player_row[i].text.lower() == 'chelsea':
                                player_dict['team'] = 6
                            elif player_row[i].text.lower() == 'crystal palace':
                                player_dict['team'] = 7
                            elif player_row[i].text.lower() == 'everton':
                                player_dict['team'] = 8
                            elif player_row[i].text.lower() == 'fulham':
                                player_dict['team'] = 9
                            elif player_row[i].text.lower() == 'liverpool':
                                player_dict['team'] = 10
                            elif player_row[i].text.lower() == 'luton':
                                player_dict['team'] = 11
                            elif player_row[i].text.lower() == 'man city':
                                player_dict['team'] = 12
                            elif player_row[i].text.lower() == 'man utd':
                                player_dict['team'] = 13
                            elif player_row[i].text.lower() == 'newcastle':
                                player_dict['team'] = 14
                            elif player_row[i].text.lower() == "nott'm forest":
                                player_dict['team'] = 15
                            elif player_row[i].text.lower() == 'sheffield utd':
                                player_dict['team'] = 16
                            elif player_row[i].text.lower() == 'spurs':
                                player_dict['team'] = 17
                            elif player_row[i].text.lower() == 'west ham':
                                player_dict['team'] = 18
                            elif player_row[i].text.lower() == 'wolves':
                                player_dict['team'] = 19
                            else:
                                raise ValueError(f'{player_row[i].text.lower()} is not registerd')
                            """
                        if i == 2:
                            continue
                        player_dict['price'] = player_row[i].text.replace('£','').lower()
                        if header == 'goalkeepers':
                            player_dict['pos'] = 0
                        elif header == 'defenders':
                            player_dict['pos'] = 1
                        elif header == 'midfielders':
                            player_dict['pos'] = 3
                        elif header == 'forwards':
                            player_dict['pos'] = 4
                        else:
                            raise ValueError('position is not registerd')

                    players_position_dict[f'{player_dict["last_name"]}-{player_dict["first_name"]}-{player_dict["pos"]}-{player_dict["team"]}'] = player_dict
        #pprint(players_position_dict)
        #print(sorted(set(d['team'] for d in players_position_dict.values())))
        #header = driver.find_element(By.CLASS_NAME, 'Layout__Main-eg6k6r-1').find_element(By.TAG_NAME, 'h3')
        #print(header.text)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        return players_position_dict