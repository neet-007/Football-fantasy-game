import React, { Suspense } from 'react'
import './FixturesAndResultsBase'
import { Outlet } from 'react-router-dom'
import FilterSection from '../../../components/FilterSection/FilterSection'

function FixturesAndResultsBase() {
  return (
    <section>
      <div>
        <FilterSection/>
      </div>
      <div>
        <Suspense fallback={<h1>Loading...</h1>}>
            <Outlet/>
        </Suspense>
      </div>
    </section>
  )
}

export default FixturesAndResultsBase