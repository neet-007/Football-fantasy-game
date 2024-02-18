import React from 'react'
import './ResultBox.css'

function ResultBox({team1Result=1, team2Result=1}) {
  return (
    <article className={`main-theme_result-box result-box_article d-flex justify-content-between align-items-center`}>
        <span>
            {team1Result}
        </span>
        <span>
            -
        </span>
        <span>
            {team2Result}
        </span>
    </article>
  )
}

export default ResultBox