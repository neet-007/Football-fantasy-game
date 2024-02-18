import React from 'react'
import { CaretUpFill, CaretDownFill, Key } from 'react-bootstrap-icons'
import Tr from '../shared/Tr/Tr'
import Td from '../shared/Td/Td'

function PositionColumn({position={position:1, up:true}}){
    return(
        <Td className='d-flex align-items-center'>
            <span>
                {position.position}
            </span>
            <span>
                {position.up == true ?
                    <CaretUpFill color='green'/>
                :position.up == false ?
                    <CaretDownFill color='red'/>
                :null
                }
            </span>
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

function TableRow({team={position:{position:1, up:true}, club:{name:'liverpool', imgUrl:''},
                        pl:28, w:10, l:1, d:12, gd:321, pts:10, form:['w', 'w', 'l', 'd', 'w'], next:''}}) {
  return (
    <Tr className={'d-flex gap-1 width-100 cap'}>
        <PositionColumn position={team.position}/>
        <ClubColumn club={team.club}/>
        <Td>
          {team.pl}
        </Td>
        <Td>
          {team.w}
        </Td>
        <Td>
          {team.d}
        </Td>
        <Td>
          {team.l}
        </Td>
        <Td>
          {team.gd}
        </Td>
        <Td className={'f-basis-20 d-flex justify-content-center gap-1'}>
            {team.form.map((status, i) => {
                return <FormCircle key={`${team.club.name + status + i}`} status={status}/>
            })}
        </Td>
        <Td>
          {team.pts}
        </Td>
        <Td>
          {team.next}
        </Td>
    </Tr>
  )
}

export default TableRow