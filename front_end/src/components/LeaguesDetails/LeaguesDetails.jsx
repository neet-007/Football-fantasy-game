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
import { useNavigate } from 'react-router-dom'
import { useGetUserLeagues } from '../../lib/queriesAndMutaions'

function LeagueTableRow({league}){
  return (
    <Tr className='leagues-details_league-table-tr'>
          <Td className='league-details_league-table-header-league'>
            <p className='cursor-pointer'>
              {league.league__name}
            </p>
            {league.position > league.last_position &&
                <span className='league-details_league-table-header-league-icon'>
                  <ChevronUp color='#9600ff'/>
                </span>
            }
            {league.position < league.last_position &&
               <span className='league-details_league-table-header-league-icon'>
                  <ChevronDown color='#9600ff'/>
               </span>
            }
            {league.position === league.last_position &&
               <span className='league-details_league-table-header-league-icon-gray'>

               </span>
            }
          </Td>
          <Td className='league-details_league-table-header-current'>
            {league.position}
          </Td>
          <Td className='league-details_league-table-header-last'>
            <p>
              {league.last_position}
            </p>
            <span className='d-flex align-items-center justify-content-center cursor-pointer'>
              <GearFill/>
            </span>
          </Td>
        </Tr>
  )
}

function LeagueTable({leagueName, leagues=[]}){
  return (
    <article>
    <SectionHeader>{leagueName}</SectionHeader>
    <table className='leagues-details_league-table-table cap'>
      <Thead>
        <Tr className='league-details_league-table-header'>
          <Th className='league-details_league-table-header-league'>
            league
          </Th>
          <Th>

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
        <Tr>
        <Td>
        <p>no {leagueName} joined yet, <InvisibleButton>craete and join leagues now</InvisibleButton></p>
        </Td>
        </Tr>
        :
        leagues.map(league => {
          return <LeagueTableRow key={`league-${league.league__name}`} league={league}/>
        })}
      </Tbody>
    </table>
    </article>
  )
}

function LeaguesDetails() {
  const {data, isLoading} = useGetUserLeagues()
  const navigate = useNavigate()

  if(isLoading) return null
  return (
    <section className='leagues-details_section'>
      <div className='league-details_buttons'>
        <Button childern='' className={'d-flex align-items-center cap'} backgroundColor={'light'}
        onClick={() => navigate('/fantasy/leagues-and-cups/create-league')}>
            <Plus size={20}/>
            <p>create & join leagues</p>
        </Button>
        <Button childern='' className={'d-flex align-items-center cap'} backgroundColor={'light'}>
            <ArrowClockwise size={20}/>
            <p>renew your leagues</p>
            <p></p>
        </Button>
      </div>
      <LeagueTable leagueName={'Invitational Classic Leagues'} leagues={data?.classic_leagues}/>
      <LeagueTable leagueName={'Invitational Head-to-Head Leagues'} leagues={data?.h2h_leagues}/>
      <LeagueTable leagueName={'Public Classic Leagues'}/>
      <LeagueTable leagueName={'Public Head-to-Head Leagues'}/>
      <LeagueTable leagueName={'General Leagues'}/>
      <LeagueTable leagueName={'Broadcaster Leagues'}/>
    </section>
  )
}

export default LeaguesDetails