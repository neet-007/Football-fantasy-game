import React from 'react'
import './ResultBox.css'

function ResultBox({homeResults=1, awayResults=1}) {
  return (
    <article className={`main-theme_result-box result-box_article d-flex justify-content-between align-items-center`}>
        <span>
            {homeResults}
        </span>
        <span>
            -
        </span>
        <span>
            {awayResults}
        </span>
    </article>
  )
}

export default ResultBox