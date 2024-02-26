import React from 'react'
import StatsList from '../../../components/StatsList/StatsList'
import { useGetStatsDashBoard } from '../../../lib/queriesAndMutaions'
import './Stats.css'

function Stats() {
  const {data, isLoading} = useGetStatsDashBoard()
  if (isLoading) return
  return (
    <section>
      {Object.keys(data).map(stat => {
        return <StatsList listName={stat} list={data[stat]}/>
      })
      }
    </section>
  )
}

export default Stats