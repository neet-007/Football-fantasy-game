import React, { useState } from 'react'
import './PlayerSmallCard.css'
import Modal from '../Modal/Modal'
import Button from '../Button/Button'

function PlayerSmallCard({name='salah', club='liverpool', points=30, gameweek=22, index, position, disabledPlayers, setDisabledPlayers}) {
  const [isOpen, setIsOpen] = useState(false)
  function handleClick(e){
    if (e.target.id === 'modal-overlay') return setIsOpen(false)
    return setIsOpen(true)
  }
  if (position === undefined) console.log(name)
  return (
    <article className='player-small-card_article' onClick={handleClick}>
        <img className='player-small-card_img' src={`${ disabledPlayers[position].indexOf(index) === -1 ? `/src/assets/${club}-shirt.webp` : '/src/assets/none-shirt.webp'}`} alt="" />
        <div className='player-small-card_name-div'>{name}</div>
        <div className='player-small-card_div'>
            <span>{gameweek}</span>
            <span>{points}</span>
        </div>
        <Modal isOpen={isOpen} className={'d-flex f-di-column gap-1 p-1 align-items-center '}>
          <p>{name}</p>
          {disabledPlayers[position].indexOf(index) !== -1&&
           <Button childern='' onClick={() => setDisabledPlayers(prev => ({...prev, [position]:prev[position].filter(x => x !== index).sort((a,b) => a - b)}))}>restore player</Button>
          }
          {disabledPlayers[position].indexOf(index) !== -1&&
           <Button childern=''>select replacment</Button>
          }
          <Button childern='' onClick={() => setDisabledPlayers(prev => ({...prev, [position]:[...prev[position], index].sort((a,b) => a-b)}))}>remove player</Button>
          <Button childern=''>player information</Button>
        </Modal>
    </article>
  )
}

export default PlayerSmallCard