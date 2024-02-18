import React from 'react'

function Th({children, ...props}) {
  return (
    <th {...props}>
        {children}
    </th>
  )
}

export default Th