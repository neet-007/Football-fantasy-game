import React from 'react'
import PlayerPointsPitch from '../../../components/PlayerPointsPitch/PlayerPointsPitch'
import SectionHeader from '../../../components/shared/SectionHeader/SectionHeader'
import Row from '../../../components/shared/Row/Row'
import Column from '../../../components/shared/Column/Column'
import LeaguesDetails from '../../../components/LeaguesDetails/LeaguesDetails'
import { Link } from 'react-router-dom'

function Points() {
  return (
    <section className='fantasy-layout_with-side-bar'>
      <div>
        <PlayerPointsPitch/>
        fixtures
      </div>
      <div>
        <article className='fantasy-layout_side-bar-section cap'>
          <div className='d-flex justify-content-between'>
              <span>
                <p>player name</p>
                <p>team name</p>
              </span>
              <span>county</span>
          </div>
          <SectionHeader>points/ranking</SectionHeader>
          <Row className={'d-flex justify-content-between'}>
            <Column>overall points</Column>
            <Column>213</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>overall ranking</Column>
            <Column>321</Column>
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
            <Column>213</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>total transfers</Column>
            <Column>321</Column>
          </Row>
          <Link>dsad</Link>
          <SectionHeader>finance</SectionHeader>
          <Row className={'d-flex justify-content-between'}>
            <Column>squad value</Column>
            <Column>213</Column>
          </Row>
          <Row className={'d-flex justify-content-between'}>
            <Column>in the bank</Column>
            <Column>321</Column>
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
    </section>
  )
}

export default Points