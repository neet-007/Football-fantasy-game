import React from 'react'
import Select from '../shared/Select/Select'
import './FilterSection.css'

function FilterSection({filters, setFilters}) {
  return (
    <div>
        {Object.keys(filters).map(filter => {
          return <>
                    <Select options={filters[filter]} setValue={setFilters} filter={filter}/>
                </>
        })}
    </div>
  )
}

export default FilterSection