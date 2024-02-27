import React, { useCallback, useMemo, useState } from 'react'
import Thead from '../../../components/shared/Thead/Thead'
import Tbody from '../../../components/shared/Tbody/Tbody'
import Tr from '../../../components/shared/Tr/Tr'
import Td from '../../../components/shared/Td/Td'
import Th from '../../../components/shared/Th/Th'
import { useGetStatsByCategory } from '../../../lib/queriesAndMutaions'
import { useParams } from 'react-router-dom'
import './Stats.css'
import FilterSection from '../../../components/FilterSection/FilterSection'
import PageSlider from '../../../components/PageSlider/PageSlider'

function PlayerStats() {
  const [page, setPage] = useState(1)
  const [filters, setFilters] = useState({})
  const [sort, setSort] = useState('decs')
  const {stat} = useParams()
  const {data, isLoading} = useGetStatsByCategory({stat:filters['stat'] ? filters['stat']: stat,
                                                  team:filters['team'] ? filters['team']: undefined,
                                                  nation:filters['nation'] ? filters['nation']: undefined,
                                                  position:filters['position'] ? filters['position']: undefined,
                                                  sort,
                                                  page})

  if (isLoading) return
  return (
    <section className='cap'>
        <h3>premier leagues players stats</h3>
        <FilterSection filters={data?.filters} setFilters={setFilters}/>
        <button onClick={() => setSort(prev => prev === 'decs' ? 'acs' : 'decs')}>sort</button>
        <table className='width-100'>
            <Thead>
                <Tr className={'player-stats_row-container width-100'}>
                    <Th>
                        player
                    </Th>
                    <Th className='player-stats_team'>
                        club
                    </Th>
                    <Th className='player-stats_nation'>
                        nationality
                    </Th>
                    <Th>
                        stat
                    </Th>
                </Tr>
            </Thead>
            <Tbody>
                {data?.stat.map(player => {
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
                            <Td className='player-stats_nation'>{player.nation}</Td>
                            <Td>{player[data?.filters['stat'][1]]}</Td>
                           </Tr>
                })}
            </Tbody>
        </table>
        <PageSlider page={page} pages={data?.page.num_of_pages} next={data?.page.next} prev={data?.page.prev} setPages={setPage}/>
    </section>
  )
}

export default PlayerStats