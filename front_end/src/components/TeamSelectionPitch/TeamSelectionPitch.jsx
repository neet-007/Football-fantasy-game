import React, { useState } from 'react'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'
import SectionHeader from '../shared/SectionHeader/SectionHeader'
import './TeamSelectionPitch.css'
import Button from '../shared/Button/Button'

function TeamSelectionPitch() {
  const [playersSelected, setPlayersSelected] = useState(0)
  const [moneyRemaining, setMoneyRemaining] = useState(100.00)
  return (
    <section className='cap'>
        <PlayerSelection pickTeam>
           <SectionHeader>
            <p>gameweek</p>
           </SectionHeader>
           <p className='d-flex justify-content-center'>deadline</p>
           <div className='d-flex gap-1'>
            <div className='f-grow-1 d-flex f-di-column'>
                <p className='align-self-center'>players selected</p>
                <p className={`align-self-center ${playersSelected === 15 ? 'backgroundColor-main-theme-utility': 'backgroundColor-red'}`}>{playersSelected} / 15</p>
                <Button childern='' className={'cap'}>auto pick</Button>
            </div>
            <div className='f-grow-1 d-flex f-di-column'>
                <p className='align-self-center'>money remaining</p>
                <p className='align-self-center'>{moneyRemaining}</p>
                <Button childern='' className={'cap'}>reset</Button>
            </div>
           </div>
        </PlayerSelection>
    </section>
  )
}

export default TeamSelectionPitch