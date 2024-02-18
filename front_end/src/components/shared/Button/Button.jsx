import React from 'react'
import './Button.css'

function Button({backgroundColor, childern='App Button'}) {
  const theme = 'main'
  return (
    <button className={`${!backgroundColor ? `${theme}-theme_button`: backgroundColor} button_button ${backgroundColor} `}>{childern}</button>
  )
}

export default Button