import React, { useState } from 'react'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'
import SectionHeader from '../shared/SectionHeader/SectionHeader'
import './TeamSelectionPitch.css'
import Button from '../shared/Button/Button'

function TeamSelectionPitch({playersList, reset, disabledPlayers, setDisapledPlayers, selectionDetails,togglePitchPlayer, team3Plus}) {

  return (
    <section className='cap'>
        <PlayerSelection teamSelection playersList={playersList} disabledPlayers={disabledPlayers} setDisabledPlayers={setDisapledPlayers} togglePitchPlayer={togglePitchPlayer} team3Plus={team3Plus}>
           <SectionHeader>
            <p>gameweek</p>
           </SectionHeader>
           <p className='d-flex justify-content-center'>deadline</p>
           <div className='d-flex gap-1'>
            <div className='f-grow-1 d-flex f-di-column'>
                <p className='align-self-center'>players selected</p>
                <p className={`align-self-center ${selectionDetails.players === 15 ? 'backgroundColor-main-theme-utility': 'backgroundColor-red'}`}>{selectionDetails.players} / 15</p>
                <Button childern='' className={'cap'}>auto pick</Button>
            </div>
            <div className='f-grow-1 d-flex f-di-column'>
                <p className='align-self-center'>money remaining</p>
                <p className={`align-self-center ${selectionDetails.money < 0 ? 'backgroundColor-red': ''}`}>{selectionDetails.money}</p>
                <Button childern='' className={'cap'} onClick={reset}>reset</Button>
            </div>
           </div>
        </PlayerSelection>
    </section>
  )
}

export default TeamSelectionPitch