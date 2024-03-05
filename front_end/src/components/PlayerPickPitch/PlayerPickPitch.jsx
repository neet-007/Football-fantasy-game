import React from 'react'
import './PlayerPickPitch.css'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'
import Button from '../shared/Button/Button'
import { usePostTeam } from '../../lib/queriesAndMutaions'

function PlayerPickPitch({playersList, selectedPlayer, positionsCounts, setSelectedPlayer, togglePickTeam, toggleTeamSwitch}) {
  const {mutateAsync:postTeam} = usePostTeam()
  function saveTeam(){
    const {captins, ...other} = playersList
    const temp = Object.values(other)
    postTeam({team:{players_pks:temp.flatMap(({starter}) => [...starter].map(x => [x.id, x.index])), bench_order:temp.flatMap(({benched}) => [...benched].sort((a,b) => a.benched_order - b.benched_order)).map(x => [x.id, x.index]).reduce((obj, value, key) => {obj[value[0]]=[key, value[1]]; return obj},{}), captins}})
  }
  return (
    <section>
        <PlayerSelection pickTeam benchRow playersList={playersList} positionsCounts={positionsCounts} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch}>
            <div className='player-pick-pitch_header-div cap'>
                <p className='player-pick-pitch_header-first-row'>game week</p>
                <p className='player-pick-pitch-header-second-row'>Gameweek 26:Sat 24 Feb 16:30</p>
            </div>
        </PlayerSelection>
        <Button childern='' onClick={saveTeam}>save team</Button>
    </section>
  )
}

export default PlayerPickPitch