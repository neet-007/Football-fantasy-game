import React from 'react'
import './TimeBox.css'

function TimeBox({time='17:20'}) {
  return (
    <article className={` time-box_article`}>{time}</article>
  )
}

export default TimeBox