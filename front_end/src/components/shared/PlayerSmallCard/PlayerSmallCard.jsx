import React, { useState } from 'react'
import './PlayerSmallCard.css'
import Modal from '../Modal/Modal'
import Button from '../Button/Button'

function PlayerSmallCard({player, disabledPlayers, togglePitchPlayer, team3Plus}) {
  const [isOpen, setIsOpen] = useState(false)

  function handleClick(e){
    if (e.target.id === 'modal-overlay') return setIsOpen(false)
    return setIsOpen(true)
  }

  return (
    <article className={`player-small-card_article ${team3Plus(player.club) ? 'backgroundColor-red':''}`} onClick={handleClick}>
        <img className='player-small-card_img' src={`${disabledPlayers[player.position].indexOf(player.index) === -1 ? `/src/assets/${player.club}-shirt.webp` : '/src/assets/none-shirt.webp'}`} alt="" />
        <div className='player-small-card_name-div'>{player.name}</div>
        <div className='player-small-card_div'>
            <span>{}</span>
            <span>{player.points}</span>
        </div>
        <Modal isOpen={isOpen} className={'d-flex f-di-column gap-1 p-1 align-items-center '}>
          <p>{player.name}</p>
          {disabledPlayers[player.position].indexOf(player.index) !== -1&&
           <Button childern='' onClick={() => togglePitchPlayer(true, player.position, player.index, parseFloat(player.price))}>restore player</Button>
          }
          {disabledPlayers[player.position].indexOf(player.index) !== -1&&
           <Button childern=''>select replacment</Button>
          }
          <Button childern='' onClick={() => togglePitchPlayer(false, player.position, player.index, parseFloat(player.price))}>remove player</Button>
          <Button childern=''>player information</Button>
        </Modal>
    </article>
  )
}

export default PlayerSmallCard