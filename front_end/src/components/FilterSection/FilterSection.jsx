import React from 'react'
import Select from '../shared/Select/Select'
import './FilterSection.css'

function FilterSection({filters, setFilters}) {
  return (
    <div>
        {Object.keys(filters).map(filter => {
          return <>
                    <Select options={filters[filter][0]} value={filters[filter][1]} setValue={setFilters} filter={filter}/>
                </>
        })}
    </div>
  )
}

/*
<select onChange={(e) => setFilters(prev => ({...prev, [filter]:e.target.value}))} value={filters[filter][1]}>
                      {filters[filter][0].map(stat =>{
                        return <option>{stat}</option>
                      })}
                    </select>
*/
export default FilterSection