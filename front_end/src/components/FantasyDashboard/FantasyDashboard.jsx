import React from 'react'
import './FantasyDashboard.css'
import Button from '../shared/Button/Button'
import InvisibleButton from '../shared/InvisibleButton/InvisibleButton'
import { ArrowRight } from 'react-bootstrap-icons'

function FantasyDashboard() {
  return (
    <nav className='fanstasy-dashborad_nav'>
        <div className='fanstasy-dashborad_header'>
            <p className='fanstasy-dashborad_header-game-week d-flex justify-content-center cap'>
                game week 25
            </p>
            <Button className='fanstasy-dashborad_header-button cap'
                    backgroundColor={'light'}
                    childern='my team'/>
            <InvisibleButton className='fanstasy-dashborad_header-prizes cap d-flex align-items-center justify-content-center'>
                prizes <ArrowRight/>
            </InvisibleButton>
            <img className='fanstasy-dashborad_header-img'/>
        </div>
        <div className='fanstasy-dashborad_options cap'>
            <InvisibleButton className={'cap d-flex f-di-column'}>
                <span className='d-flex align-items-center'>
                    <p>highest points</p>
                    <ArrowRight/>
                </span>
                <p>126</p>
            </InvisibleButton>
            <span className='d-flex f-di-column'>
                <p>
                    average points
                </p>
                <p>
                    25
                </p>
            </span>
            <span className='d-flex f-di-column'>
                <p>
                    transfers made
                </p>
                <p>
                    213415
                </p>
            </span>
            <span className='d-flex f-di-column'>
                <p>
                    most transferd in
                </p>
                <p>
                    you
                </p>
            </span>
            <span className='d-flex f-di-column'>
                <p>
                    wildcards player
                </p>
                <p>
                    54564
                </p>
            </span>
            <span className='d-flex f-di-column'>
                <p>
                    most captained
                </p>
                <p>
                    dasda
                </p>
            </span>
        </div>
    </nav>
  )
}

export default FantasyDashboard