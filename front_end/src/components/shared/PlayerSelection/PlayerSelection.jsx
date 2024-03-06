import React, { useState } from 'react'
import PitchSvg from '../PitchSvg'
import './PlayerSelection.css'
import Button from '../Button/Button'
import PlayerSmallCard from '../PlayerSmallCard/PlayerSmallCard'
import Row from '../Row/Row'
import Column from '../Column/Column'

function PlayerSelection({benchRow, pickTeam, transfer, teamSelection, playersList, selectedPlayer, setSelectedPlayer, positionsCounts, disabledPlayers={}, togglePitchPlayer, setTransferDetails, togglePickTeam, toggleTeamSwitch,team3Plus, children, ...props}) {
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
                        return <PlayerSmallCard key={`gk-s-${player.id}`} pickTeam={pickTeam} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.goalkeepers.benched.map(player => {
                        return <PlayerSmallCard key={`gk-b-${player.id}`} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className='player-selection_pitch-defenders-row'>
                {
                    playersList.defenders.starter.map(player => {
                        return <PlayerSmallCard key={`d-s-${player.id}`} pickTeam={pickTeam} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.defenders.benched.map(player => {
                        return <PlayerSmallCard key={`d-b-${player.id}`} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className='player-selection_pitch-midfielders-row'>
                {
                    playersList.midfielders.starter.map(player => {
                        return <PlayerSmallCard key={`m-s-${player.id}`} pickTeam={pickTeam} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.midfielders.benched.map(player => {
                        return <PlayerSmallCard key={`m-b-${player.id}`} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className='player-selection_pitch-strikers-row'>
                {
                    playersList.strikers.starter.map(player => {
                        return <PlayerSmallCard key={`s-s-${player.id}`} pickTeam={pickTeam} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
                {(transfer || teamSelection) &&
                    playersList.strikers.benched.map(player => {
                        return <PlayerSmallCard key={`s-b-${player.id}`} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
            </span>
            <span className={`player-selection_pitch-bench-row ${benchRow ? 'player-selection_pitch-bench-row-show' : 'player-selection_pitch-bench-row-hide'}`}>
                {
                    playersList.goalkeepers.benched.concat(playersList.defenders.benched).concat(playersList.midfielders.benched).concat(playersList.strikers.benched).sort((a,b) => a.benched_order - b.benched_order).map(player => {
                        return <PlayerSmallCard key={`b-b-${player.id}`} pickTeam={pickTeam} player={player} captin={playersList.captins?.captin === player.id} viceCaptin={playersList.captins?.vice_captin === player.id} benched={true} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch} team3Plus={team3Plus}/>
                    })
                }
            </span>
        </div>
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