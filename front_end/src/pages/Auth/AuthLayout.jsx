import React, { Suspense } from 'react'
import './AuthLayout.css'
import { Link, Outlet, useLocation } from 'react-router-dom'
import Navbar from '../../components/Navbar/Navbar'

function AuthLayout() {
  const {pathname} = useLocation()
  const path = pathname.replace('/auth/','')
  return (
    <main>
        <Navbar/>
        <section className='auth-layout_section'>
            <h3 className='auth-layout_header'>{path}</h3>
            <Suspense>
                <Outlet/>
            </Suspense>
            <p>
                {path === 'signup' ?
                'have an account ? '
                :
                `dont have an account ? `}
                <Link to={path === 'signup' ?
                '/auth/login'
                :
                '/auth/signup'}>
                {path === 'signup' ?
                'login'
                :
                'signup'}
                </Link>
            </p>
        </section>
    </main>
  )
}

export default AuthLayout