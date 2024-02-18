import React from 'react'
import './Row.css'

function Row({className, children}) {
  return (
    <div className={`main-theme_row ${className}`}>
        {children}
    </div>
  )
}

export default Row