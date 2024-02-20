import React from 'react'
import PitchSvg from '../PitchSvg'
import './PlayerSelection.css'
import Button from '../Button/Button'
import PlayerSmallCard from '../PlayerSmallCard/PlayerSmallCard'

function PlayerSelection({benchRow, children}) {
  return (
    <article className='player-selection_article'>
        <div className='player-selection_header'>
            {children}
        </div>
        <div className='player-selection_toggle-view'>
            <Button childern='pitch view' backgroundColor={'gray'}/>
            <Button childern='list view' backgroundColor={'gray'}/>
        </div>
        <div className='player-selection_pitch'>
            <PitchSvg className='player-selection_pitch-pitch'/>
            <span className='player-selection_pitch-goal-keeper-row'>
                <PlayerSmallCard/>
            </span>
            <span className='player-selection_pitch-defenders-row'>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
            </span>
            <span className='player-selection_pitch-midfielders-row'>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
            </span>
            <span className='player-selection_pitch-strikers-row'>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
            </span>
            <span className={`player-selection_pitch-bench-row ${benchRow ? 'player-selection_pitch-bench-row-show' : 'player-selection_pitch-bench-row-hide'}`}>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
                <PlayerSmallCard/>
            </span>
        </div>
    </article>
  )
}

export default PlayerSelection