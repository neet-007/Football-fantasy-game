import React from 'react'
import './Column.css'

function Column({className, children}) {
  return (
    <div className={`${className} main-theme_column`}>
        {children}
    </div>
  )
}

export default Column