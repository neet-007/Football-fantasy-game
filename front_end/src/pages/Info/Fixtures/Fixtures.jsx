import React from 'react'
import './Fixtures.css'
import { useGetTeamsFixtures } from '../../../lib/queriesAndMutaions'
import MatchResultCard from '../../../components/MatchResultCard/MatchResultCard'
function Fixtures() {
  const {data} = useGetTeamsFixtures()
  return (
      <>
        {data?.map(team => {
          return <MatchResultCard homeTeam={team.team.name} awayTeam={team.opponent.name}/>
        })}
      </>
  )
}

export default Fixtures