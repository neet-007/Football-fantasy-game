import React from 'react'
import './Fixtures.css'
import { useGetTeamsFixtures } from '../../../lib/queriesAndMutaions'
import MatchResultCard from '../../../components/MatchResultCard/MatchResultCard'
function Fixtures() {
  const {data, isLoading} = useGetTeamsFixtures()
  if (isLoading) return
  return (
      <>
        {Object.keys(data).map(date => {
          console.log(date)
          return (
            <>
              <p>{date}</p>
              {data[date].map(team => {
                return <MatchResultCard homeTeam={team.team.name} awayTeam={team.opponent.name} time={team.time}/>
              })}
            </>
          )
        })
        }
      </>
  )
}

export default Fixtures