import React, { useState } from 'react'
import Button from '../shared/Button/Button'
import InvisibleButton from '../shared/InvisibleButton/InvisibleButton'
import { NavLink } from 'react-router-dom'
import {useMainContext} from '../../context/MainContext'
import './FantasyNavbar.css'

function FantasyNavbar() {
  const {user} = useMainContext()
  console.log(user)
  const [isMoreOpen, setIsMoreOpen] = useState(false)

  return (
    <nav className='fantasy-nav-bar_nav'>
        <p className='fantasy-nav-bar_header cap'>fantasy</p>
        <ul className='fantasy-nav-bar_ul'>
            <li>
                <NavLink to={'status'}>
                    <Button childern='status' className='cap cursor-pointer'/>
                </NavLink>
            </li>
            {(user.has_team && !user.made_first_team) &&
            <li>
                <NavLink to={'team-selection'}>
                    <Button childern='' className='cap cursor-pointer'>
                        team selection
                    </Button>
                </NavLink>
            </li>
            }
            {user.made_first_team &&
            <>
            <li>
                <NavLink to={'points'}>
                    <Button childern='points' className='cap cursor-pointer'/>
                </NavLink>
            </li>
            <li>
                <NavLink to={'pick-team'}>
                    <Button childern='pick team' className='cap cursor-pointer'/>
                </NavLink>
            </li>
            <li>
                <NavLink to={'transfers'}>
                    <Button childern='transfers' className='cap cursor-pointer'/>
                </NavLink>
            </li>
            </>
            }
            <li className='fantasy-nav-bar_more-menu-container'>
                <Button childern='more' className='cap cursor-pointer' onClick={()=>setIsMoreOpen(prev => !prev)}/>
                <ul className={`${isMoreOpen ? 'fantasy-nav-bar_mobile-ul-open':'fantasy-nav-bar_mobile-ul-close'} fantasy-nav-bar_mobile-ul`}>
                    {user.made_first_team&&
                    <li>
                        <InvisibleButton className='cap'>league & cups</InvisibleButton>
                    </li>
                    }
                    <li>
                        <InvisibleButton className='cap'>fixtures</InvisibleButton>
                    </li>
                    <li>
                        <InvisibleButton className='cap'>stats</InvisibleButton>
                    </li>
                </ul>
            </li>
            {user.made_first_team&&
            <li>
                <NavLink to={'leagues-and-cups'}>
                    <Button childern='leagues & cups' className='cap cursor-pointer'/>
                </NavLink>
            </li>
            }
            <li>
                <NavLink to={'fixtures'}>
                    <Button childern='fixtures' className='cap cursor-pointer'/>
                </NavLink>
            </li>
            <li>
                <NavLink to={'stats'}>
                    <Button childern='stats' className='cap cursor-pointer'/>
                </NavLink>
            </li>
        </ul>
    </nav>
  )
}

export default FantasyNavbar