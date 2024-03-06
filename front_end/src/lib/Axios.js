import axios from 'axios'

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const config = {
    headers: {
      'Accept':'application/json',
      'Content-type':'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    }
}

export async function getCsrfToken(){
    try {
        let res = await axios.get('/api/auth/get-csrftoken')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function register({email, password, rePassword}){
    try {
        let res = await axios.post('/api/auth/register', {email, password, re_password:rePassword}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function login({email, password}){
    try {
        let res = await axios.post('/api/auth/login', {email, password}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function logout(){
    try {
        let res = await axios.post('/api/auth/logout', {}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function checkUser(){
    try {
        let res = await axios.get('/api/auth/check-user', {}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function postTeamCreation({name , favoriteTeamPk}){
    try {
        let res = await axios.post('/api/team/team/', {name, favorite_team_pk:favoriteTeamPk}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getPremierLeagueBaseTeams(){
    try {
        let res = await axios.get('/api/premier-league/teams/base_teams_list/')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getPremierLeagueTable(){
    try {
        let res = await axios.get('/api/premier-league/teams/')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getTeamsFixtures(){
    try {
        let res = await axios.get('/api/premier-league/fixtures/fixtures/')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getTeamsResults(){
    try {
        let res = await axios.get('/api/premier-league/fixtures/results/')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getStatsDashBoard(){
    try {
        let res = await axios.get('/api/player-info/players/dashboard/')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getStatsByCategory({stat, team, nation, position, sort, page}){
    try {
        let res = await axios.get(`/api/player-info/players/stats/?${stat ? `stat=${stat}&selected_stat=${stat}&`:''}${team ? `club=${team}&selected_club=${team}&`:''}${nation ? `nation=${nation}&selected_nation=${nation}&`:''}${position ? `position=${position}&selected_position=${position}&`:''}${sort ? `sort=${sort}&`:''}${page ? `page=${page}&`:''}`)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getStatsFantasy({team, position, sort, page}){
    try {
        let res = await axios.get(`/api/player-info/players/fantasy_stats/?${team ? `club=${team}&selected_club=${team}&`:''}${position ? `position=${position}&selected_position=${position}&`:''}${sort ? `sort=${sort}&`:''}${page ? `page=${page}&`:''}`)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getPlayersFantasy({team, position, sort, page}){
    try {
        let res = await axios.get(`/api/player-info/players/fantasy_players/?${team ? `club=${team}&selected_club=${team}&`:''}${position ? `position=${position}&selected_position=${position}&`:''}${sort ? `sort=${sort}&`:''}${page ? `page=${page}&`:''}`)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getInjuries({team, status, position, sort, page}){
    try {
        let res = await axios.get(`/api/player-info/injuries?${team ? `club=${team}&selected_club=${team}&`:''}${status ? `club=${status}&selected_club=${status}&`:''}${position ? `position=${position}&selected_position=${position}&`:''}${sort ? `sort=${sort}&`:''}${page ? `page=${page}&`:''}`)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function getUserTeam(){
    try {
        let res = await axios.get('/api/team/game-week-team/user_team/')
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function postTeam({team}){
    try {
        console.log(team)
        let res = await axios.post('/api/team/game-week-team/', team, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function postTransfers({team}){
    try {
        let res = await axios.post('/api/team/game-week-team/player_transfer/', team, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function postLeagueClassic({name, startingGameWeek}){
    try {
        let res = await axios.post('/api/league/league/', {name, starting_game_week:startingGameWeek}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}
export async function postLeagueH2H({name, startingGameWeek, isH2H, allowPostCreattionEntry}){
    try {
        let res = await axios.post('/api/league/league/', {name, starting_game_week:startingGameWeek, is_h2h:isH2H, allow_post_create_entry:allowPostCreattionEntry}, config)
        console.log(res.data)
        return res.data
    } catch (error) {
        console.log(error)
    }
}