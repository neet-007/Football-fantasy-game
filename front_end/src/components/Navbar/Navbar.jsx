import React, { useRef, useState } from 'react'
import './Navbar.css'
import { List, X } from 'react-bootstrap-icons'
import { NavLink } from 'react-router-dom'
import { useMainContext } from '../../context/MainContext'
import InvisibleButton from '../shared/InvisibleButton/InvisibleButton'
import { useLogout } from '../../lib/queriesAndMutaions'
import { CSRFToken } from '../shared/CSRFToken'

function Navbar() {
  const {isAuthenticated} = useMainContext()
  const {mutateAsync:logout} = useLogout()
  const [isOpen, setIsOpen] = useState(false)
  const menuRef = useRef()

  function toggleMenu(){
    if (isOpen) menuRef.current.style.maxWidth = '0'
    if (!isOpen) menuRef.current.style.maxWidth = '50%'
    setIsOpen(prev => !prev)
  }

  return (
    <nav className={`main-theme_nav-bar nav-bar_nav`}>
        <img className='nav-bar_nav-img' src="/src/assets/pl-logo.png"/>
        <div className='nav-bar_div'>
            <span className='nav-bar_span-user-search'>
                {isAuthenticated ?
                    <span className='cursor-pointer'>
                        user
                    </span>
                :
                    <InvisibleButton onClick={logout}>
                        <CSRFToken/>
                        logout
                    </InvisibleButton>
                }
                <span className='cursor-pointer'>
                    search
                </span>
            </span>
            <p className='nav-bar_ul-icon cursor-pointer' onClick={toggleMenu}>
                {isOpen ?
                    <X size={30}/>
                    :
                    <List size={30}/>
                }
            </p>
            <div className='nav-bar_ul-wrapper' ref={menuRef}>
                <ul className='nav-bar_ul'>
                    <li className='cursor-pointer'>
                        <NavLink className={'txt-decoration clr-inherit cap'}
                        to='/'>
                            home
                        </NavLink>
                    </li>
                    <li className='cursor-pointer'>
                        <NavLink className={'txt-decoration clr-inherit cap'}
                        to='/fixtures'>
                            fixtures
                        </NavLink>
                    </li>
                    <li className='cursor-pointer'>
                        <NavLink className={'txt-decoration clr-inherit cap'}
                        to='/results'>
                            results
                        </NavLink>
                    </li>
                    <li className='cursor-pointer'>
                        <NavLink className={'txt-decoration clr-inherit cap'}
                        to='/tables'>
                            tables
                        </NavLink>
                    </li>
                    <li className='cursor-pointer'>
                        <NavLink className={'txt-decoration clr-inherit cap'}
                        to='/fantasy'>
                            fantasy
                        </NavLink>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
  )
}

export default Navbar