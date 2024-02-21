import React from 'react'
import './SectionHeader.css'

function SectionHeader({children, ...props}) {
  return (
    <h3 className={`main-theme_section-header_h3 section-header_h3`} {...props}>
      {children}
    </h3>
  )
}

export default SectionHeader