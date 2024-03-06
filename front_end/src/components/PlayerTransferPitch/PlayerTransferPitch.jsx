import React from 'react'
import './PlayerTransferPitch.css'
import Button from '../shared/Button/Button'
import PlayerSelection from '../shared/PlayerSelection/PlayerSelection'
import { usePostTransfers } from '../../lib/queriesAndMutaions'

function PlayerTransferPitch({transferDetails, setTransferDetails, playersList, reset, disabledPlayers, togglePitchPlayer, team3Plus}) {
    const {mutateAsync:postTransfers} = usePostTransfers()
    function makeTransfers(){
    const {captins, ...other} = playersList
    const temp = Object.values(other)
    postTransfers({team:{players_pks:temp.flatMap(({starter}) => [...starter]).map(x => [x.id, x.index]),
    bench_order:temp.flatMap(({benched}) => [...benched]).sort((a,b) => a.bench_order - b.bench_order).map(x => [x.id, x.index]).reduce((acc, curr, index) => {
        acc[curr[0]] = [index, curr[1]]
        return acc
    },{}),
    captins,
    transfers_dict:Object.keys(transferDetails.playersTransferd).reduce((acc, curr) => {
        acc[curr.slice(0, curr.indexOf('-'))] = transferDetails.playersTransferd[curr]
        return acc
    },{})}})
  }

    return (
    <section>
        <PlayerSelection transfer playersList={playersList} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} setTransferDetails={setTransferDetails} team3Plus={team3Plus}>
            <div className='player-transfer-pitch_header cap'>
                <p className='player-transfer-pitch_header-game-week'>game week</p>
                <div className='player-transfer-pitch-header-transfer-warning'>
                    {team3Plus &&
                    <p>
                        cant have more than 3 players from the same team
                    </p>
                    }
                </div>
                <p className='player-transfer-pitch_header-game-week-date'>dsadsadsadsadsadsad</p>
                <span className='player-transfer-pitch_header-transfers'>
                    <p>free transfers</p>
                    <p>{transferDetails.freeTransfers}</p>
                </span>
                <span className='player-transfer-pitch_header-cost'>
                    <p>cost</p>
                    <p>{transferDetails.cost} pts</p>
                </span>
                <span className='player-transfer-pitch_header-money'>
                    <p>money remaining</p>
                    <p>{transferDetails.moneyRemaining}</p>
                </span>
                <Button childern='' className='player-transfer-pitch_header-auto-pick'>auto pick</Button>
                <Button childern='' className='player-transfer-pitch_header-reset' onClick={reset}>reset</Button>
                <Button childern='' className='player-transfer-pitch_header-wild-card'>wild card</Button>
            </div>
        </PlayerSelection>
        <Button childern='' onClick={makeTransfers}>transfer</Button>
    </section>
  )
}

export default PlayerTransferPitch