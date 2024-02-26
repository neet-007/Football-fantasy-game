import React from 'react'
import { CaretUpFill, CaretDownFill, Key } from 'react-bootstrap-icons'
import Tr from '../shared/Tr/Tr'
import Td from '../shared/Td/Td'

function PositionColumn({position}){
    return(
        <Td className='d-flex align-items-center'>
            <span>
                {position}
            </span>
            {/*
            <span>
                {position.up == true ?
                    <CaretUpFill color='green'/>
                :position.up == false ?
                    <CaretDownFill color='red'/>
                :null
                }
            </span>
            */}
        </Td>
    )
}

function ClubColumn({club={name:'liverpool', imgUrl:''}}){
    return(
        <Td className='f-basis-30 d-flex align-items-center gap-1 justify-content-start'>
            <span>
                <img src={club.imgUrl}/>
            </span>
            <span>
                {club.name}
            </span>
        </Td>
    )
}

function FormCircle({status}){
    return(
        <span className={`border-radius-circle d-flex align-items-center justify-content-center p-3
        ${status === 'w' ? 'backgroundColor-win' : status === 'l' ? 'backgroundColor-loss' : status === 'd' ? 'backgroundColor-draw' : ''}`}>
            {status}
        </span>
    )
}

function TableRow({team={postition:1, base_team:{name:'liverpool', imgUrl:''},
                        pl:28, wins:10, losses:1, draws:12, gd:321, pts:10, form:['w', 'w', 'l', 'd', 'w'], next:''}}) {
  return (
    <Tr className={'d-flex gap-1 width-100 cap'}>
        <PositionColumn position={team.postition}/>
        <ClubColumn club={team.base_team}/>
        <Td>
          {team.matches_played}
        </Td>
        <Td>
          {team.wins}
        </Td>
        <Td>
          {team.draws}
        </Td>
        <Td>
          {team.losses}
        </Td>
        <Td>
          {team.goals_differance}
        </Td>
        <Td className={'f-basis-20 d-flex justify-content-center gap-1'}>
            {team.last_five?.split(' ').map((status, i) => {
                return <FormCircle key={`${team.base_team.name + status + i}`} status={status}/>
            })}
        </Td>
        <Td>
          {team.points}
        </Td>
        <Td>
          {team.next}
        </Td>
    </Tr>
  )
}

export default TableRow