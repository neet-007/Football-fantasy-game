import React, { Suspense } from 'react'
import { Outlet } from 'react-router-dom'
import Navbar from '../../components/Navbar/Navbar'
import './InfoLayout.css'

function InfoLayout() {
  return (
    <main>
        <Navbar/>
        <Suspense fallback={<h1>Loading...</h1>}>
            <Outlet>

            </Outlet>
        </Suspense>
    </main>
  )
}

export default InfoLayout