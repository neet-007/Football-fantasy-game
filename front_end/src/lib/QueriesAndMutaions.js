import {useQuery, useMutation} from '@tanstack/react-query'
import { login, logout, register } from './axios'

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