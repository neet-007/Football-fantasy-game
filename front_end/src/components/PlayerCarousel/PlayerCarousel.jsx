import React, { useRef } from 'react'
import './PlayerCarousel.css'
import PlayerSmallCard from '../shared/PlayerSmallCard/PlayerSmallCard'
import InvisibleButton from '../shared/InvisibleButton/InvisibleButton'
import { StarFill, ChevronLeft, ChevronRight} from 'react-bootstrap-icons'


function PlayerCarousel() {
  const sliderRef = useRef()

  function handleScroll(dir){
    if (dir === 'left'){
      sliderRef.current.scrollBy({
        left: - sliderRef.current.offsetWidth * 33/100,
        behavior: "smooth",
      })
    }
    if (dir === 'rigth'){
      sliderRef.current.scrollBy({
        left: sliderRef.current.offsetWidth * 33/100,
        behavior: "smooth",
      })
    }
  }
  return (
    <article className={`main-theme_player-carousel_container player-carousel_container cap`}>
        <div className='player-carousel_header'>
            <span className='player-carousel_icon-span'>
                <StarFill color='#04e762'/>
            </span>
            <h3>2023/24 player of the week</h3>
        </div>
        <section className='player-carousel_slider-container'>
          <InvisibleButton onClick={() => handleScroll('left')}>
            <ChevronLeft/>
            </InvisibleButton>
          <div className="player-carousel_slider" ref={sliderRef}>
            <PlayerSmallCard/>
            <PlayerSmallCard/>
            <PlayerSmallCard/>
            <PlayerSmallCard/>
            <PlayerSmallCard/>
            <PlayerSmallCard/>
            <PlayerSmallCard/>
            <PlayerSmallCard/>
          </div>
          <InvisibleButton onClick={() => handleScroll('rigth')}>
            <ChevronRight/>
            </InvisibleButton>
        </section>
    </article>
  )
}

export default PlayerCarousel