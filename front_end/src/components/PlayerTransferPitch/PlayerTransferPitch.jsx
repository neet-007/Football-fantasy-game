import React, {useState} from 'react'
import './PlayerTransferPitch.css'
import Button from '../shared/Button/Button'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'

function PlayerTransferPitch({userTeam, playersList, reset, disabledPlayers, setDisapledPlayers}) {
  const [playersSelected, setPlayersSelected] = useState(0)
  const [moneyRemaining, setMoneyRemaining] = useState(100.00)
  return (
    <section>
        <PlayerSelection transfer playersList={playersList} disabledPlayers={disabledPlayers} setDisabledPlayers={setDisapledPlayers}>
            <div className='player-transfer-pitch_header cap'>
                <p className='player-transfer-pitch_header-game-week'>game week</p>
                <p className='player-transfer-pitch_header-game-week-date'>dsadsadsadsadsadsad</p>
                <span className='player-transfer-pitch_header-transfers'>
                    <p>free transfers</p>
                    <p>{userTeam.free_transfers}</p>
                </span>
                <span className='player-transfer-pitch_header-cost'>
                    <p>cost</p>
                    <p>0 pts</p>
                </span>
                <span className='player-transfer-pitch_header-money'>
                    <p>money remaining</p>
                    <p>{userTeam.bank}</p>
                </span>
                <Button className='player-transfer-pitch_header-auto-pick'/>
                <Button className='player-transfer-pitch_header-reset'/>
                <Button className='player-transfer-pitch_header-wild-card'/>
            </div>
        </PlayerSelection>
    </section>
  )
}

export default PlayerTransferPitch