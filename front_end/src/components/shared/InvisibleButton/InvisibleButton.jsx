import React from 'react'

function InvisibleButton({className, children, ...props}) {
  return (
    <button className={`${className} invisible-btn`} {...props}>{children}</button>
  )
}

export default InvisibleButton