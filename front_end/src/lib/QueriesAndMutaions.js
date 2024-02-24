import {useQuery, useMutation} from '@tanstack/react-query'
import { getPremierLeagueTable, getTeamsFixtures, getTeamsResults, login, logout, register } from './axios'

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