import {useQuery, useMutation} from '@tanstack/react-query'
import { checkUser, getInjuries, getPlayersFantasy, getPremierLeagueBaseTeams, getPremierLeagueTable, getStatsByCategory, getStatsDashBoard, getStatsFantasy, getTeamsFixtures, getTeamsResults, getUserTeam, login, logout, postLeagueClassic, postLeagueH2H, postTeam, postTeamCreation, postTransfers, register } from './axios'

export function useRegister(){
    return useMutation({
        mutationFn: ({email, password, rePassword}) => register({email, password, rePassword})
    })
}

export function useLogin(){
    return useMutation({
        mutationFn: ({email, password}) => login({email, password})
    })
}

export function useLogout(){
    return useMutation({
        mutationFn: logout
    })
}

export function usePostTeamCreation(){
    return useMutation({
        mutationFn:({name, favoriteTeamPk}) => postTeamCreation({name, favoriteTeamPk})
    })
}

export function useCheckUser(){
    return useQuery({
        queryKey:['check-user'],
        queryFn:checkUser
    })
}

export function useGetPremierLeagueBaseTeams(){
    return useQuery({
        queryKey:['premier-league-base-teams'],
        queryFn:getPremierLeagueBaseTeams
    })
}

export function useGetPremierLeagueTable(){
    return useQuery({
        queryKey: ['premier-league-teams'],
        queryFn:getPremierLeagueTable
    })
}

export function useGetTeamsFixtures(){
    return useQuery({
        queryKey: ['premier-league-fixtures'],
        queryFn:getTeamsFixtures
    })
}

export function useGetTeamsResults(){
    return useQuery({
        queryKey: ['premier-league-results'],
        queryFn:getTeamsResults
    })
}

export function useGetStatsDashBoard(){
    return useQuery({
        queryKey: ['premier-league-stats-dashboard'],
        queryFn:getStatsDashBoard
    })
}

export function useGetStatsByCategory({stat, team, nation, position, sort, page}){
    return useQuery({
        queryKey: ['premier-league-stats-by-category', stat, team, nation, position, sort, page],
        queryFn: () =>  getStatsByCategory({stat, team, nation, position, sort, page})
    })
}

export function useGetStatsFanstasy({team, position, sort, page}){
    return useQuery({
        queryKey: ['premier-league-stats-fantasy', team, position, sort, page],
        queryFn: () => getStatsFantasy({team, position, sort, page})
    })
}

export function useGetPlayersFanstasy({team, position, sort, page}){
    return useQuery({
        queryKey: ['premier-league-players-fantasy', team, position, sort, page],
        queryFn: () => getPlayersFantasy({team, position, sort, page})
    })
}

export function useGetInjuries({team, status, position, sort, page}){
    return useQuery({
        queryKey: ['premier-league-stats-fantasy', team, position, sort, page],
        queryFn: () => getInjuries({team, position, sort, page})
    })
}

export function useGetUserTeam(){
    return useQuery({
        queryKey: ['team-game-week-team-user-team'],
        queryFn:getUserTeam
    })
}

export function usePostTeam(){
    return useMutation({
        mutationFn: ({team}) => postTeam({team})
    })
}

export function usePostTransfers(){
    return useMutation({
        mutationFn: ({team}) => postTransfers({team})
    })
}

export function usePostLeagueClassic(){
    return useMutation({
        mutationFn: ({name, startingGameWeek}) => postLeagueClassic({name, startingGameWeek})
    })
}

export function usePostLeagueH2H(){
    return useMutation({
        mutationFn: ({name, startingGameWeek, isH2H, allowPostCreattionEntry}) => postLeagueH2H({name, startingGameWeek, isH2H, allowPostCreattionEntry})
    })
}