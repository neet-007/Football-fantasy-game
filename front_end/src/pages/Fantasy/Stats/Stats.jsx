import React, { useState } from 'react'
import { useGetStatsFanstasy } from '../../../lib/queriesAndMutaions'
import FilterSection from '../../../components/FilterSection/FilterSection'
import Thead from '../../../components/shared/Thead/Thead'
import Tbody from '../../../components/shared/Tbody/Tbody'
import Th from '../../../components/shared/Th/Th'
import Tr from '../../../components/shared/Tr/Tr'
import Td from '../../../components/shared/Td/Td'
import SectionHeader from '../../../components/shared/SectionHeader/SectionHeader'
import './Stats.css'
import PageSlider from '../../../components/PageSlider/PageSlider'

function Stats() {
  const [page, setPage] = useState(1)
  const [filters, setFilters] = useState()
  const {data, isLoading} = useGetStatsFanstasy({team:filters?.team, position:filters?.position, sort:filters?.sort, page})
  if (isLoading) return
  return (
    <section>
      <FilterSection filters={data?.filters} setFilters={setFilters}/>
      <SectionHeader>
        sorted by:{data?.filters.sort[1]}
      </SectionHeader>
      <table className='width-100 cap'>
        <Thead className={'fantasy-stats_row-container'}>
          <Th>player</Th>
          <Th>club</Th>
          <Th>points</Th>
          <Th>price</Th>
        </Thead>
        <Tbody>
            {data?.stat.map(player => {
              return <Tr className='fantasy-stats_row-container'>
                        <Td className='d-flex f-di-column'>
                          {player.last_name ?
                            <span>{player.last_name}</span>
                            :
                            <span>{player.first_name}</span>
                          }
                          <span>{player.position === 0 ?
                                'GK'
                                :
                                player.position === 1 ?
                                'DEF'
                                :
                                player.position === 3 ?
                                'MID'
                                :
                                player.position === 4 ?
                                'FWD'
                                :
                                ''

                          }</span>
                        </Td>
                        <Td className='fantasy-stats_team'>
                          {player.team__name}
                        </Td>
                        <Td>
                          {player.overall_points}
                        </Td>
                        <Td>
                          {player.price}
                        </Td>
                     </Tr>
            })}
        </Tbody>
      </table>
      <PageSlider page={page} pages={data?.page.num_of_pages} next={data?.page.next} prev={data?.page.prev} setPages={setPage}/>
    </section>
  )
}

export default Stats