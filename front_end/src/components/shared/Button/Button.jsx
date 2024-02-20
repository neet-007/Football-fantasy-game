import React from 'react'
import './Button.css'

function Button({className, clicked, backgroundColor, childern='App Button', ...props}) {
  const theme = 'main'
  return (
    <button className={`${!backgroundColor ? `${theme}-theme_button`: `backgroundColor-${backgroundColor}`} button_button ${className}
                        ${clicked ? 'main-theme_button-clicked':''}`}
            {...props}>{childern}</button>
  )
}

export default Button