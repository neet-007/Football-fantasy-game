import React from 'react'
import './Thead.css'

function Thead({className, children, ...props}) {
  return (
    <thead className={`main-theme_thead ${className}`} {...props}>
        {children}
    </thead>
  )
}

export default Thead