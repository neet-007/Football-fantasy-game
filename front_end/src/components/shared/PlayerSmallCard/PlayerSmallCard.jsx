import React, { useState } from 'react'
import './PlayerSmallCard.css'
import Modal from '../Modal/Modal'
import Button from '../Button/Button'
import { X } from 'react-bootstrap-icons'

function PlayerSmallCard({name='salah', club='liverpool', points=30, gameweek=22}) {
  const [isOpen, setIsOpen] = useState(false)
  const [isDisabled, setIsDisabled] = useState(false)
  function handleClick(e){
    if (e.target.id === 'modal-overlay') return setIsOpen(false)
    return setIsOpen(true)
  }
  return (
    <article className='player-small-card_article' onClick={handleClick}>
        <img className='player-small-card_img' src={`/src/assets/${club}-shirt.webp`} alt="" />
        <div className='player-small-card_name-div'>{name}</div>
        <div className='player-small-card_div'>
            <span>{gameweek}</span>
            <span>{points}</span>
        </div>
        <Modal isOpen={isOpen} className={'d-flex f-di-column gap-1 p-1 align-items-center '}>
          <p>{name}</p>
          {isDisabled &&
           <Button childern=''>restore player</Button>
          }
          {isDisabled &&
           <Button childern=''>select replacment</Button>
          }
          <Button childern=''>remove player</Button>
          <Button childern=''>player information</Button>
        </Modal>
    </article>
  )
}

export default PlayerSmallCard