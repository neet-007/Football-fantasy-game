import React from 'react'
import './PlayerSelectionFilter.css'
import FilterSection from '../FilterSection/FilterSection'

function PlayerSelectionFilter({filters, setFilters}) {
  return (
    <div>
        <FilterSection filters={filters} setFilters={setFilters}/>
    </div>
  )
}

export default PlayerSelectionFilter