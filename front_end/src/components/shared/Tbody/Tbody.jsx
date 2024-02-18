import React from 'react'
import './Tbody.css'

function Tbody({className, children, ...props}) {
  return (
    <tbody className={`main-theme_tbody ${className}`} {...props}>
        {children}
    </tbody>
  )
}

export default Tbody