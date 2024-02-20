import React from 'react'
import './PlayerCarousel.css'
import { StarFill } from 'react-bootstrap-icons'

function PlayerCarousel() {
  return (
    <article className={`main-theme_player-carousel_container player-carousel_container cap`}>
        <div className='player-carouesl_header d-flex align-items-center gap-1'>
            <span className='player-carousel_icon-span'>
                <StarFill color='#04e762'/>
            </span>
            <h3>2023/24 player of the week</h3>
        </div>
        <div className='player-carousel_slider'></div>
    </article>
  )
}

export default PlayerCarousel