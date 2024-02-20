import React from 'react'
import './PlayerSmallCard.css'

function PlayerSmallCard({name='salah', club='liverpool', points=30, gameweek=22}) {
  return (
    <article className='player-small-card_article'>
        <img className='player-small-card_img' src={`/src/assets/${club}-shirt.webp`} alt="" />
        <div className='player-small-card_name-div'>{name}</div>
        <div className='player-small-card_div'>
            <span>{gameweek}</span>
            <span>{points}</span>
        </div>
    </article>
  )
}

export default PlayerSmallCard