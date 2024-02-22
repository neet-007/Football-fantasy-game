import React, { Suspense } from 'react'
import { Outlet } from 'react-router-dom'
import Navbar from '../../components/Navbar/Navbar'
import './FantasyLayout.css'
import FantasyNavbar from '../../components/FantasyNavbar/FantasyNavbar'

function FantasyLayout() {
  return (
    <main>
        <Navbar/>
        <FantasyNavbar/>
        <Suspense>
            <Outlet>

            </Outlet>
        </Suspense>
    </main>
  )
}

export default FantasyLayout