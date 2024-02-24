import React from 'react'
import PlayerPointsPitch from '../../../components/PlayerPointsPitch/PlayerPointsPitch'
import SectionHeader from '../../../components/shared/SectionHeader/SectionHeader'
import Row from '../../../components/shared/Row/Row'
import Column from '../../../components/shared/Column/Column'
import LeaguesDetails from '../../../components/LeaguesDetails/LeaguesDetails'
import { Link } from 'react-router-dom'
import TeamSideBar from '../../../components/TeamSideBar/TeamSideBar'

function Points() {
  return (
    <section className='fantasy-layout_with-side-bar'>
      <div>
        <PlayerPointsPitch/>
        fixtures
      </div>
      <TeamSideBar/>
    </section>
  )
}

export default Points