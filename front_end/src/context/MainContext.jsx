import React, {useState, useEffect, createContext, useContext} from "react";

const INITIAL_USER = {

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