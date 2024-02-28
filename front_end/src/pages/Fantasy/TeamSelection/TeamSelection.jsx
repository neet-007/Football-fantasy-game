import React from 'react'
import './TeamSelection.css'
import TeamSelectionPitch from '../../../components/TeamSelectionPitch/TeamSelectionPitch'

function TeamSelection() {
  return (
    <section className='fantasy-layout_with-side-bar'>
      <div>
        <TeamSelectionPitch/>
        fixtures
      </div>
      <div></div>
    </section>
  )
}

export default TeamSelection