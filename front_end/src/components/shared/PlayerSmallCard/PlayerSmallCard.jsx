import React, { useState } from 'react'
import './PlayerSmallCard.css'
import Modal from '../Modal/Modal'
import Button from '../Button/Button'

function PlayerSmallCard({pickTeam, player, captin, viceCaptin, disabledPlayers={}, togglePitchPlayer=() => {}, togglePickTeam, team3Plus=() => {}}) {
  const [isOpen, setIsOpen] = useState(false)

  function handleClick(e){
    if (e.target.id === 'modal-overlay') return setIsOpen(false)
    return setIsOpen(true)
  }
  if (captin) console.log(player.name)
  return (
    <article className={`player-small-card_article ${team3Plus(player.club) ? 'backgroundColor-red':''}`} onClick={handleClick}>
        {pickTeam ?
        captin ?
        <p>C</p>
        :
        viceCaptin ?
        <p>V</p>
        :
        null
        :
        null
        }
        {pickTeam ?
        <img className='player-small-card_img' src={`/src/assets/${player.club}-shirt.webp`} alt="" />
        :
        <img className='player-small-card_img' src={`${disabledPlayers[player.position].indexOf(player.index) === -1 ? `/src/assets/${player.club}-shirt.webp` : '/src/assets/none-shirt.webp'}`} alt="" />
        }
        <div className='player-small-card_name-div'>{player.name}</div>
        <div className='player-small-card_div'>
            <span>{}</span>
            <span>{player.points}</span>
        </div>
        {pickTeam ?
        <Modal isOpen={isOpen} className={'d-flex f-di-column gap-1 p-1 align-items-center '}>
          <p>{player.name}</p>
          {
           <Button childern='' >switch</Button>
          }
          {!player.captin &&
           <Button childern='' onClick={() => togglePickTeam(player, captin=true)}>make captin</Button>
          }
          {!player.vice_captin &&
           <Button childern='' onClick={() => togglePickTeam(player, viceCaptin=true)}>make vice captin</Button>
          }
          <Button childern=''>player information</Button>
        </Modal>
        :
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
        }

    </article>
  )
}

export default PlayerSmallCard