import React from 'react'
import TeamSideBar from '../../../components/TeamSideBar/TeamSideBar'
import PlayerPickPitch from '../../../components/PlayerPickPitch/PlayerPickPitch'

function PickTeam() {
  return (
    <section className='fantasy-layout_with-side-bar cap'>
      <div>
        <p>pick team - team</p>
        <PlayerPickPitch/>
        results
      </div>
      <TeamSideBar/>
    </section>
  )
}

export default PickTeam