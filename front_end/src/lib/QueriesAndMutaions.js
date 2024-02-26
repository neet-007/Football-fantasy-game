import {useQuery, useMutation} from '@tanstack/react-query'
import { getPremierLeagueTable, getStatsByCategory, getStatsDashBoard, getTeamsFixtures, getTeamsResults, login, logout, register } from './axios'

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

export function useGetStatsByCategory({stat, team, nation, position}){
    return useQuery({
        queryKey: ['premier-league-stats-by-category', stat, team, nation, position],
        queryFn: () =>  getStatsByCategory({stat, team, nation, position})
    })
}