import React from 'react'

function Td({children, ...props}) {
  return (
    <td {...props}>
        {children}
    </td>
  )
}

export default Td