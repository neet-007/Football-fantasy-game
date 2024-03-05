import React, { useState } from 'react'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'
import SectionHeader from '../shared/SectionHeader/SectionHeader'
import './TeamSelectionPitch.css'
import Button from '../shared/Button/Button'
import { usePostTeam } from '../../lib/queriesAndMutaions'

function TeamSelectionPitch({playersList, reset, disabledPlayers, setDisapledPlayers, selectionDetails,togglePitchPlayer, team3Plus}) {
  const {mutateAsync:postTeam} = usePostTeam()

  function makeTeam(){
    const temp = Object.values(playersList)
    postTeam({team:{players_pks:temp.flatMap(({starter}) => [...starter].map(x => [x.id, x.index])), bench_order:temp.flatMap(({benched}) => [...benched].map(x => [x.id, x.index])).reduce((obj, key, value) => {obj[key[0]]=[value, key[1]]; return obj},{}), captins:{captin:temp.flatMap(({starter}) => [...starter]).map(x => x.id)[7], vice_captin:temp.flatMap(({starter}) => [...starter]).map(x => x.id)[8]}}})
  }

  return (
    <section className='cap'>
        <PlayerSelection teamSelection playersList={playersList} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} team3Plus={team3Plus}>
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
        {(selectionDetails.money > 0.00 && selectionDetails.players === 15) &&
          <Button childern='' onClick={makeTeam}>dsad</Button>
        }
    </section>
  )
}

export default TeamSelectionPitch