import React from 'react'
import LeagueTable from '../../../components/LeagueTable/LeagueTable'
import { useGetPremierLeagueTable } from '../../../lib/queriesAndMutaions'
import './Tables.css'

function Tables() {
  const {data} = useGetPremierLeagueTable()
  return (
    <section>
      <LeagueTable teams={data}/>
    </section>
  )
}

export default Tables