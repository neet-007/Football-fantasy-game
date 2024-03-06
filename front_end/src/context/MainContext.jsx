import React, {useState, useEffect, createContext, useContext} from "react";
import { checkUser } from "../lib/axios";

const INITIAL_USER = {
    pk:undefined,
    is_verified:undefined,
    is_admin:undefined,
    has_team:undefined,
    made_first_team:undefined
}

const INITIAL_STATE = {
    user: INITIAL_USER,
    setUser: () => {},
    isAuthenticated: false,
    setIsAuthenticated: () =>{},
    isDark: false,
    setIsDark: () => {}
}

const mainContext = createContext(INITIAL_STATE)


export function MainContextProvider({children}){
    const [user, setUser] = useState(INITIAL_USER)
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const [isDark, setIsDark] = useState(false)

    useEffect(() => {
        checkUser().then(res => {
            if (res?.error){
                setUser(INITIAL_USER)
                setIsAuthenticated(false)
            }
            setUser(res?.success)
            setIsAuthenticated(true)
        })
    },[])

    const value = {
        user:user,
        setUser:setUser,
        isAuthenticated:isAuthenticated,
        setIsAuthenticated:setIsAuthenticated,
        isDark:isDark,
        setIsDark:setIsDark
    }
    return(
        <mainContext.Provider value={value}>
            {children}
        </mainContext.Provider>
    )
}

export const useMainContext = () => useContext(mainContext)