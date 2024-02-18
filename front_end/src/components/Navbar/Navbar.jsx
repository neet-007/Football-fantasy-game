import React, { useRef, useState } from 'react'
import './Navbar.css'
import { List, X } from 'react-bootstrap-icons'

function Navbar() {
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
                <span className='cursor-pointer'>
                    user
                </span>
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
                    <li className='cursor-pointer'>home</li>
                    <li className='cursor-pointer'>fixture</li>
                    <li className='cursor-pointer'>results</li>
                    <li className='cursor-pointer'>table</li>
                    <li className='cursor-pointer'>fantasy</li>
                </ul>
            </div>
        </div>
    </nav>
  )
}

export default Navbar