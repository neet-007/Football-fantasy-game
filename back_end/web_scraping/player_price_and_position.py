from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.premier_league_utils import get_extreme_abbrieviated_preimer_league_team_int
from utils.player_info_utils import split_name


FPL_WEBSITE = 'https://fantasy.premierleague.com/player-list'

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

                        if i == 1:
                            player_dict['team'] = get_extreme_abbrieviated_preimer_league_team_int(player_row[i].text.lower())

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

    except Exception as e:
        print(e)
    finally:
        driver.quit()
        players_position_dict['first_last_dict'] = first_last_dict
        players_position_dict['last_dict'] = last_dict
        players_position_dict['first_dict'] = first_dict
        return players_position_dict

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

                        if i == 1:
                            player_dict['team'] = get_extreme_abbrieviated_preimer_league_team_int(player_row[i].text.lower())

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

    except Exception as e:
        print(e)
    finally:
        driver.quit()
        return players_position_dict