import React, { useState } from 'react'
import Thead from '../../../components/shared/Thead/Thead'
import Tbody from '../../../components/shared/Tbody/Tbody'
import Tr from '../../../components/shared/Tr/Tr'
import { useGetInjuries } from '../../../lib/queriesAndMutaions'
import FilterSection from '../../../components/FilterSection/FilterSection'

function Injuries() {
  const [page, setPage] = useState(1)
  const [filters, setFilters] = useState()
  const {data, isLoading} = useGetInjuries({team:filters?.team, status:filters?.status, position:filters?.position, sort:filters?.sort, page})

  if (isLoading) return
  return (
    <section>
        <FilterSection filters={data?.filters} setFilters={setFilters}/>
        <table>
            <Thead>
                <Tr></Tr>
            </Thead>
            <Tbody>

            </Tbody>
        </table>
    </section>
  )
}

export default Injuries