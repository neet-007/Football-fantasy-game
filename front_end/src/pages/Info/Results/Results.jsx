import React from 'react'
import './Results.css'
import { useGetTeamsResults } from '../../../lib/queriesAndMutaions'
import MatchResultCard from '../../../components/MatchResultCard/MatchResultCard'

function Results() {
  const {data} = useGetTeamsResults()
  return (
    <>
      {data?.map(team => {
        return <MatchResultCard homeTeam={team.team.name} awayTeam={team.opponent.name}
                                homeResults={team.goals_for} awayResults={team.goals_against}/>
      })}
    </>
  )
}

export default Results