from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

FPL_WEBSITE = 'https://fantasy.premierleague.com/player-list'

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

def get_fpl_data():
    driver = webdriver.Chrome()
    driver.get(url=FPL_WEBSITE)
    try:
        sleep(30)
        containers = driver.find_elements(By.CLASS_NAME, 'Layout__Main-eg6k6r-1')
        for container in containers:
            header = container.find_element(By.TAG_NAME, 'h3').text.lower()
            keepers_dict = {}
            tables = container.find_elements(By.TAG_NAME, 'tbody')
            for table in tables:
                table_row = table.find_elements(By.TAG_NAME, 'tr')
                for tr in table_row:
                    keeper_dict = {}
                    player_row = tr.find_elements(By.TAG_NAME, 'td')
                    for i in range(len(player_row)):
                        if i == 0:
                            name = player_row[i].text.lower().split(' ')
                            name_length = len(name)
                            #get_long_part = lambda name_str: max(name_str.split('.'), key=lambda x: len(x)) if len(name_str.split('.')) >= 2 else None
                            if name_length == 1:
                                keeper_dict['first_name'] = None
                                keeper_dict['middle_name'] = None
                                keeper_dict['last_name'] = get_long_part(name[0])
                            if name_length == 2:
                                keeper_dict['first_name'] = get_long_part(name[0])
                                keeper_dict['middle_name'] = None
                                keeper_dict['last_name'] = get_long_part(name[1])
                            if name_length == 3:
                                keeper_dict['first_name'] = get_long_part(name[0])
                                keeper_dict['middle_name'] = get_long_part(name[1])
                                keeper_dict['last_name'] = get_long_part(name[2])
                        if i == 1:
                            #keeper_dict['team'] = player_row[i].text.lower()
                            if player_row[i].text.lower() == 'arsenal':
                                keeper_dict['team'] = 0
                            elif player_row[i].text.lower() == 'aston villa':
                                keeper_dict['team'] = 1
                            elif player_row[i].text.lower() == 'brentford':
                                keeper_dict['team'] = 2
                            elif player_row[i].text.lower() == 'brighton':
                                keeper_dict['team'] = 3
                            elif player_row[i].text.lower() == 'bournemouth':
                                keeper_dict['team'] = 4
                            elif player_row[i].text.lower() == 'burnley':
                                keeper_dict['team'] = 5
                            elif player_row[i].text.lower() == 'chelsea':
                                keeper_dict['team'] = 6
                            elif player_row[i].text.lower() == 'crystal palace':
                                keeper_dict['team'] = 7
                            elif player_row[i].text.lower() == 'everton':
                                keeper_dict['team'] = 8
                            elif player_row[i].text.lower() == 'fulham':
                                keeper_dict['team'] = 9
                            elif player_row[i].text.lower() == 'liverpool':
                                keeper_dict['team'] = 10
                            elif player_row[i].text.lower() == 'luton':
                                keeper_dict['team'] = 11
                            elif player_row[i].text.lower() == 'man city':
                                keeper_dict['team'] = 12
                            elif player_row[i].text.lower() == 'man utd':
                                keeper_dict['team'] = 13
                            elif player_row[i].text.lower() == 'newcastle':
                                keeper_dict['team'] = 14
                            elif player_row[i].text.lower() == "nott'm forest":
                                keeper_dict['team'] = 15
                            elif player_row[i].text.lower() == 'sheffield utd':
                                keeper_dict['team'] = 16
                            elif player_row[i].text.lower() == 'spurs':
                                keeper_dict['team'] = 17
                            elif player_row[i].text.lower() == 'west ham':
                                keeper_dict['team'] = 18
                            elif player_row[i].text.lower() == 'wolves':
                                keeper_dict['team'] = 19
                            else:
                                raise ValueError(f'{player_row[i].text.lower()} is not registerd')
                        if i == 2:
                            continue
                        keeper_dict['price'] = player_row[i].text.replace('£','').lower()
                        if header == 'goalkeepers':
                            keeper_dict['pos'] = 0
                        elif header == 'defenders':
                            keeper_dict['pos'] = 1
                        elif header == 'midfielders':
                            keeper_dict['pos'] = 3
                        elif header == 'forwards':
                            keeper_dict['pos'] = 4
                        else:
                            raise ValueError('position is not registerd')
                    keepers_dict[player_row[0].text.lower()] = keeper_dict
                pprint(keepers_dict)
                print(sorted(set(d['team'] for d in keepers_dict.values())))
        #header = driver.find_element(By.CLASS_NAME, 'Layout__Main-eg6k6r-1').find_element(By.TAG_NAME, 'h3')
        #print(header.text)
    finally:
        driver.quit()
    """
    request = requests.get(url=FPL_WEBSITE)
    soup = BeautifulSoup(request.content, 'html.parser')

    players_tables = soup.find('div', {'id':'root'}).find_all('div')
    print(players_tables)
    """