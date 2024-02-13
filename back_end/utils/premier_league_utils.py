def get_premier_league_team_int(team:str) -> int:
    team = team.lower().strip()
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
    raise ValueError(f'{team} is not registerd')

def get_verbose_premier_league_team_int(team:str) -> int:
        if team == 'arsenal':
            return 0
        if team == 'aston villa':
            return 1
        if team == 'brentford':
            return 2
        if team == 'brighton and hove albion':
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
        if team == 'manchester united':
            return 13
        if team == 'newcastle united':
            return 14
        if team == 'nottingham forest':
            return 15
        if team == 'sheffield united':
            return 16
        if team == 'tottenham hotspur':
            return 17
        if team == 'west ham united':
            return 18
        if team == 'wolverhampton wanderers':
            return 19
        raise ValueError(f'{team} is not registerd')