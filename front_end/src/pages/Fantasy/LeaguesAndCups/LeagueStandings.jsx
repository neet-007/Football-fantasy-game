import React from 'react'
import { useParams } from 'react-router-dom'
import { useGetLeagueStandings } from '../../../lib/queriesAndMutaions'

function LeagueStandings() {
  const {id} = useParams()
  const {data, isLoading} = useGetLeagueStandings({id})

  if (isLoading) return null
  return (
    <section>LeagueStandings</section>
  )
}

export default LeagueStandings