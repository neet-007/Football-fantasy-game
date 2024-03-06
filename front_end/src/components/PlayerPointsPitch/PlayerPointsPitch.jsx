import React, { useState } from 'react'
import './PlayerPointsPitch.css'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'
import InvisibleButton from '../shared/InvisibleButton/InvisibleButton'
import { ArrowRight, ChevronLeft, ChevronRight, StarFill } from 'react-bootstrap-icons'

function PlayerPointsPitch({userTeam}) {
  const [playersList, setPlayersList] = useState(userTeam.players)
  return (
    <section>
        <PlayerSelection benchRow playersList={playersList} disabledPlayers={{0:[], 1:[], 3:[], 4:[]}}>
            <div className='player-points-pitch_header'>
                <div className='player-points-pitch_header-first-row cap'>
                    <InvisibleButton>
                        <ChevronLeft/>
                    </InvisibleButton>
                    <p>game week</p>
                    <InvisibleButton>
                        <ChevronRight/>
                    </InvisibleButton>
                </div>
                <div className='player-points-pitch_header-second-row cap'>
                    <div className='player-points-pitch_header-second-row-average'>
                        <p>
                            average points
                        </p>
                        <p>
                           50
                        </p>
                    </div>
                    <div className='player-points-pitch_header-second-row-highest'>
                        <InvisibleButton>
                            highest points
                        </InvisibleButton>
                        <p>
                            120
                        </p>
                    </div>
                    <div className='player-points-pitch_header-second-row-main'>
                        <p>
                            latest points
                        </p>
                        <p>
                            {userTeam.team.overall_points}
                        </p>
                        <span>
                            a
                        </span>
                    </div>
                    <div className='player-points-pitch_header-second-row-rank'>
                        <p>
                            GW rank
                        </p>
                        <p>
                            {userTeam.team.overall_rank}
                        </p>
                    </div>
                    <div className='player-points-pitch_header-second-row-transfers'>
                        <InvisibleButton>
                            transfers
                        </InvisibleButton>
                        <p>0</p>
                    </div>
                </div>
                <InvisibleButton className='player-points-pitch_header-third-row cap'>
                    <span className='player-points-pitch_header-third-row-icon'>
                        <StarFill color='#04e762'/>
                    </span>
                    <p>team of the week</p>
                    <ArrowRight/>
                </InvisibleButton>
            </div>
        </PlayerSelection>
    </section>
  )
}

export default PlayerPointsPitch