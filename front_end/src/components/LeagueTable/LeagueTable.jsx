import React from 'react'
import Thead from '../shared/Thead/Thead'
import TableHeader from './TableHeader'
import TableRow from './TableRow'

function LeagueTable({teams=[]}) {
  return (
    <table className='width-100 p-1'>
        <Thead>
            <TableHeader/>
        </Thead>
        <tbody className='d-flex f-di-column gap-1'>
            {teams.map(team => {
              return <TableRow team={team}/>
            })}
        </tbody>
    </table>
  )
}

export default LeagueTable