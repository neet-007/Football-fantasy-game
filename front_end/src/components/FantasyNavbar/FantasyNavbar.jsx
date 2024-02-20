import React, { useRef, useState } from 'react'
import './FantasyNavbar.css'
import Button from '../shared/Button/Button'
import InvisibleButton from '../shared/InvisibleButton/InvisibleButton'
function FantasyNavbar() {
  const [isMoreOpen, setIsMoreOpen] = useState(false)

  return (
    <nav className='fantasy-nav-bar_nav'>
        <p className='fantasy-nav-bar_header cap'>fantasy</p>
        <ul className='fantasy-nav-bar_ul'>
            <li>
                <Button childern='status' className='cap cursor-pointer' clicked/>
            </li>
            <li>
                <Button childern='points' className='cap cursor-pointer'/>
            </li>
            <li>
                <Button childern='pick team' className='cap cursor-pointer'/>
            </li>
            <li>
                <Button childern='transfers' className='cap cursor-pointer'/>
            </li>
            <li className='fantasy-nav-bar_more-menu-container'>
                <Button childern='more' className='cap cursor-pointer' onClick={()=>setIsMoreOpen(prev => !prev)}/>
                <ul className={`${isMoreOpen ? 'fantasy-nav-bar_mobile-ul-open':'fantasy-nav-bar_mobile-ul-close'} fantasy-nav-bar_mobile-ul`}>
                    <li>
                        <InvisibleButton className='cap'>league & cups</InvisibleButton>
                    </li>
                    <li>
                        <InvisibleButton className='cap'>fixtures</InvisibleButton>
                    </li>
                    <li>
                        <InvisibleButton className='cap'>stats</InvisibleButton>
                    </li>
                </ul>
            </li>
            <li>
                <Button childern='leagues & cups' className='cap cursor-pointer'/>
            </li>
            <li>
                <Button childern='fixtures' className='cap cursor-pointer'/>
            </li>
            <li>
                <Button childern='stats' className='cap cursor-pointer'/>
            </li>
        </ul>
    </nav>
  )
}

export default FantasyNavbar