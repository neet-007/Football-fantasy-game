import React from 'react'
import Row from '../shared/Row/Row'
import Column from '../shared/Column/Column'
import SectionHeader from '../shared/SectionHeader/SectionHeader'
import LeaguesDetails from '../LeaguesDetails/LeaguesDetails'
import { Link } from 'react-router-dom'

function TeamSideBar({userTeam}) {
  return (
    <div>
        <article className='fantasy-layout_side-bar-section cap'>
            <div className='d-flex justify-content-between'>
                <span>
                    <p>{userTeam.user.name}</p>
                    <p>{userTeam.name}</p>
                </span>
                <span>county</span>
            </div>
          <SectionHeader>points/ranking</SectionHeader>
          <Row className={'d-flex justify-content-between'}>
            <Column>overall points</Column>
            <Column>{userTeam.overall_points}</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>overall ranking</Column>
            <Column>{userTeam.overall_rank}</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>total players</Column>
            <Column>213</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>gameweek points</Column>
            <Column>2133</Column>
          </Row>
          <Link>dsad</Link>
        </article>
        <LeaguesDetails/>
        <article className='fantasy-layout_side-bar-section cap'>
          <div>
              <p>transfers and finance</p>
          </div>
          <SectionHeader>transfers</SectionHeader>
          <Row className={'d-flex justify-content-between'}>
            <Column>gameweek transfers</Column>
            <Column>{userTeam.game_week_transfers_made}</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>total transfers</Column>
            <Column>321</Column>
          </Row>
          <Link>dsad</Link>
          <SectionHeader>finance</SectionHeader>
          <Row className={'d-flex justify-content-between'}>
            <Column>squad value</Column>
            <Column>{userTeam.team_value}</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>in the bank</Column>
            <Column>{userTeam.bank}</Column>
          </Row>
        </article>
        <article className='fantasy-layout_side-bar-section cap'>
          <div>
            <p>
              admin
            </p>
          </div>
          <Link>dsad</Link>
          <Link>dsad</Link>
        </article>
      </div>
  )
}

export default TeamSideBar