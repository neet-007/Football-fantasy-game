import React, { useState } from 'react'
import PitchSvg from '../PitchSvg'
import './PlayerSelection.css'
import Button from '../Button/Button'
import PlayerSmallCard from '../PlayerSmallCard/PlayerSmallCard'
import Row from '../Row/Row'
import Column from '../Column/Column'

function PlayerSelection({benchRow, pickTeam, transfer, teamSelection, playersList, disabledPlayers, togglePitchPlayer, setTransferDetails, togglePickTeam, team3Plus, children, ...props}) {
    console.log(playersList.captins)
    return (
    <article className='player-selection_article' {...props}>
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
                {
                    playersList.goalkeepers.starter.map(player => {
                        return <PlayerSmallCard pickTeam player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.goalkeepers.benched.map(player => {
                        return <PlayerSmallCard player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className='player-selection_pitch-defenders-row'>
                {
                    playersList.defenders.starter.map(player => {
                        return <PlayerSmallCard pickTeam player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.defenders.benched.map(player => {
                        return <PlayerSmallCard player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className='player-selection_pitch-midfielders-row'>
                {
                    playersList.midfielders.starter.map(player => {
                        return <PlayerSmallCard pickTeam player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.midfielders.benched.map(player => {
                        return <PlayerSmallCard player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className='player-selection_pitch-strikers-row'>
                {
                    playersList.strikers.starter.map(player => {
                        return <PlayerSmallCard pickTeam player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.strikers.benched.map(player => {
                        return <PlayerSmallCard player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className={`player-selection_pitch-bench-row ${benchRow ? 'player-selection_pitch-bench-row-show' : 'player-selection_pitch-bench-row-hide'}`}>
                {
                    playersList.goalkeepers.benched.concat(playersList.midfielders.benched).concat(playersList.strikers.benched).sort((a,b) => a.benched_order - b.benched_order).map(player => {
                        return <PlayerSmallCard pickTeam player={player} captin={playersList.captins.captin === player.id} viceCaptin={playersList.captins.vice_captin === player.id} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} team3Plus={team3Plus}/>
                    })
                }
            </span>
        </div>
        {transfer &&
        <div className='player-selection_transfer'>
            <Button className={`width-100`} childern='transfers'/>
        </div>
        }
        {pickTeam &&
        <Row className='player-selection_pick-team cap'>
            <Column className={'d-flex f-di-column gap-1'}>
                <p className='align-self-center'>bench boost</p>
                <Button className={'cap f-grow-1'} childern='play'/>
            </Column>
            <Column className={'d-flex f-di-column gap-1'}>
                <p className='align-self-center'>triple captain</p>
                <Button className={'cap f-grow-1'} childern='play'/>
            </Column>
            <Column className={'d-flex f-di-column gap-1'}>
                <p className='align-self-center'>free hit</p>
                <Button className={'cap f-grow-1'} childern='play'/>
            </Column>
        </Row>
        }
    </article>
  )
}

export default PlayerSelection