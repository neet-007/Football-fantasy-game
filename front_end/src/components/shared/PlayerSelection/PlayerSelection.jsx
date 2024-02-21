import React from 'react'
import PitchSvg from '../PitchSvg'
import './PlayerSelection.css'
import Button from '../Button/Button'
import PlayerSmallCard from '../PlayerSmallCard/PlayerSmallCard'
import Row from '../Row/Row'
import Column from '../Column/Column'

function PlayerSelection({benchRow, pickTeam, transfer, children}) {
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