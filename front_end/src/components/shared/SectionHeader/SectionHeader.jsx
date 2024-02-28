import React from 'react'
import './SectionHeader.css'

function SectionHeader({className,  children, ...props}) {
  return (
    <h3 className={`main-theme_section-header_h3 section-header_h3 ${className}`} {...props}>
      {children}
    </h3>
  )
}

export default SectionHeader