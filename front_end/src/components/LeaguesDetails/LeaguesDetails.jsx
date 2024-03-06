import React from 'react'
import Button from '../shared/Button/Button'
import './LeaguesDetails.css'
import { ArrowClockwise, ChevronDown, ChevronUp, GearFill, Plus } from 'react-bootstrap-icons'
import SectionHeader from '../shared/SectionHeader/SectionHeader'
import Thead from '../shared/Thead/Thead'
import Tbody from '../shared/Tbody/Tbody'
import Th from '../shared/Th/Th'
import Tr from '../shared/Tr/Tr'
import Td from '../shared/Td/Td'
import InvisibleButton from '../shared/InvisibleButton/InvisibleButton'

function LeagueTableRow({league}){
  return (
    <Tr className='leagues-details_league-table-tr'>
          <Td className='league-details_league-table-header-league'>
            <p className='cursor-pointer'>
              {league.leageu}
            </p>
            {league.change === 'up' &&
                <span className='league-details_league-table-header-league-icon'>
                  <ChevronUp color='#9600ff'/>
                </span>
            }
            {league.change === 'down' &&
               <span className='league-details_league-table-header-league-icon'>
                  <ChevronDown color='#9600ff'/>
               </span>
            }
            {league.change === 'none' &&
               <span className='league-details_league-table-header-league-icon-gray'>

               </span>
            }
          </Td>
          <Td className='league-details_league-table-header-current'>
            {league.currentRank}
          </Td>
          <Td className='league-details_league-table-header-last'>
            <p>
              {league.lastRank}
            </p>
            <span className='d-flex align-items-center justify-content-center cursor-pointer'>
              <GearFill/>
            </span>
          </Td>
        </Tr>
  )
}

function LeagueTable({leagueName, leagues=[{leageu:'league', currentRank:2, lastRank:4, change:'none'}, {leageu:'league2', currentRank:2, lastRank:4, change:'down'}, {leageu:'league3', currentRank:2, lastRank:4, change:'up'}]}){
  return (
    <article>
    <SectionHeader>{leagueName}</SectionHeader>
    <table className='leagues-details_league-table-table cap'>
      <Thead className={'league-details_league-table-header'}>
        <Tr>
          <Th className='league-details_league-table-header-league'>
            league
          </Th>
        <Th className='league-details_league-table-header-current'>
          current rank
        </Th>
        <Th className='league-details_league-table-header-last'>
          last rank
        </Th>
        </Tr>
      </Thead>
      <Tbody className={'d-flex f-di-column gap-1'}>
        {(!leagues || leagues.length === 0) ?
        <p>no {leagueName} joined yet, <InvisibleButton>craete and join leagues now</InvisibleButton></p>
        :
        leagues.map(league => {
          return <LeagueTableRow key={`league-${league.leageu}`} league={league}/>
        })}
      </Tbody>
    </table>
    </article>
  )
}

function LeaguesDetails() {
  return (
    <section className='leagues-details_section'>
      <div className='league-details_buttons'>
        <Button childern='' className={'d-flex align-items-center cap'} backgroundColor={'light'}>
            <Plus size={20}/>
            <p>create & join leagues</p>
        </Button>
        <Button childern='' className={'d-flex align-items-center cap'} backgroundColor={'light'}>
            <ArrowClockwise size={20}/>
            <p>renew your leagues</p>
            <p></p>
        </Button>
      </div>
      <LeagueTable leagueName={'Invitational Classic Leagues'}/>
      <LeagueTable leagueName={'Invitational Head-to-Head Leagues'}/>
      <LeagueTable leagueName={'Public Classic Leagues'}/>
      <LeagueTable leagueName={'Public Head-to-Head Leagues'}/>
      <LeagueTable leagueName={'General Leagues'}/>
      <LeagueTable leagueName={'Broadcaster Leagues'}/>
    </section>
  )
}

export default LeaguesDetails