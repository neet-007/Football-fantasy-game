import React, { useState } from 'react'
import Thead from '../../../components/shared/Thead/Thead'
import Tbody from '../../../components/shared/Tbody/Tbody'
import Tr from '../../../components/shared/Tr/Tr'
import Td from '../../../components/shared/Td/Td'
import Th from '../../../components/shared/Th/Th'
import { useGetStatsByCategory } from '../../../lib/queriesAndMutaions'
import { useParams } from 'react-router-dom'
import './Stats.css'
import FilterSection from '../../../components/FilterSection/FilterSection'

function PlayerStats() {
  const [filters, setFilters] = useState({})
  const {stat} = useParams()
  const {data, isLoading} = useGetStatsByCategory({stat:filters['stat'] ? filters['stat']: stat,
                                                  team:filters['team'] ? filters['team']: undefined,
                                                  nation:filters['nation'] ? filters['nation']: undefined,
                                                  position:filters['position'] ? filters['position']: undefined})
  console.log(filters)
  if(isLoading) return
  return (
    <section className='cap'>
        <h3>premier leagues players stats</h3>
        <FilterSection filters={data.filters} setFilters={setFilters}/>
        <table className='width-100'>
            <Thead className={'player-stats_row-container width-100'}>
                <Th>
                    player
                </Th>
                <Th className='player-stats_team'>
                    club
                </Th>
                <Th>
                    nationality
                </Th>
                <Th>
                    stat
                </Th>
            </Thead>
            <Tbody>
                {data.stat.map(player => {
                    return <Tr className='player-stats_row-container'>
                            <Td className='d-flex gap-1'>
                                {player.first_name &&
                                <span>
                                    {player.first_name}
                                </span>
                                }
                                {player.last_name &&
                                <span>
                                    {player.last_name}
                                </span>
                                }
                            </Td>
                            <Td className='player-stats_team'>{player.team__name}</Td>
                            <Td>{player.nation}</Td>
                            <Td>{player.goals}</Td>
                           </Tr>
                })}
            </Tbody>
        </table>
    </section>
  )
}

export default PlayerStats