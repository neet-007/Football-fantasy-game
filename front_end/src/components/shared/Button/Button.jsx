import React from 'react'
import './Button.css'

function Button({className, clicked, backgroundColor, childern='App Button', children, noBorder, ...props}) {
  const theme = 'main'
  return (
    <button className={`${!backgroundColor ? `${theme}-theme_button`: `backgroundColor-${backgroundColor}`} button_button ${className}
                        ${clicked ? 'main-theme_button-clicked':''} ${noBorder ? 'button_no-border' : ''}`}
            {...props}>{childern}{children}</button>
  )
}

export default Button