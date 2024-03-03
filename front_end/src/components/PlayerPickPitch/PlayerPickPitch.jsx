import React from 'react'
import './PlayerPickPitch.css'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'

function PlayerPickPitch({playersList, togglePickTeam}) {
  return (
    <section>
        <PlayerSelection pickTeam benchRow playersList={playersList} togglePickTeam={togglePickTeam}>
            <div className='player-pick-pitch_header-div cap'>
                <p className='player-pick-pitch_header-first-row'>game week</p>
                <p className='player-pick-pitch-header-second-row'>Gameweek 26:Sat 24 Feb 16:30</p>
            </div>
        </PlayerSelection>
    </section>
  )
}

export default PlayerPickPitch