import React from 'react'

function Tr({children, ...props}) {
  return (
    <tr {...props}>
        {children}
    </tr>
  )
}

export default Tr