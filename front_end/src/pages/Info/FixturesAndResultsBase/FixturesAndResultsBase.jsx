import React, { Suspense } from 'react'
import './FixturesAndResultsBase'
import { Outlet } from 'react-router-dom'

function FixturesAndResultsBase() {
  return (
    <section>
      <div>
        filters
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