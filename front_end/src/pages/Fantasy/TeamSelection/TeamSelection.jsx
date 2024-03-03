import React, { useEffect, useMemo, useState } from 'react'
import './TeamSelection.css'
import TeamSelectionPitch from '../../../components/TeamSelectionPitch/TeamSelectionPitch'
import { useGetPlayersFanstasy } from '../../../lib/queriesAndMutaions'
import PlayerSelectionFilter from '../../../components/PlayerSelectionFilter/PlayerSelectionFilter'
import SectionHeader from '../../../components/shared/SectionHeader/SectionHeader'
import Thead from '../../../components/shared/Thead/Thead'
import Tbody from '../../../components/shared/Tbody/Tbody'
import Tr from '../../../components/shared/Tr/Tr'
import Th from '../../../components/shared/Th/Th'
import Td from '../../../components/shared/Td/Td'
import InvisibleButton from '../../../components/shared/InvisibleButton/InvisibleButton'
import Modal from '../../../components/shared/Modal/Modal'
import Button from '../../../components/shared/Button/Button'
import PageSlider from '../../../components/PageSlider/PageSlider'

const CONDITION = {
  0:2,
  1:5,
  3:5,
  4:3
}

const AA = {
  goalkeepers: {
      starter: [{ index: 0, id:undefined, name: undefined, club: undefined, points: undefined, position:0 }],
      benched: [{ index: 1, id:undefined, name: undefined, club: undefined, points: undefined, position:0 }]
  },
  defenders: {
      starter: [
          { index: 2, id:undefined, name: undefined, club: undefined, points: undefined, position:1 },
          { index: 3, id:undefined, name: undefined, club: undefined, points: undefined, position:1 },
          { index: 4, id:undefined, name: undefined, club: undefined, points: undefined, position:1 },
          { index: 5, id:undefined, name: undefined, club: undefined, points: undefined, position:1 },
      ],
      benched: [{ index: 6, id:undefined, name: undefined, club: undefined, points: undefined, position:1 }]
  },
  midfielders: {
      starter: [
          { index: 7, id:undefined, name: undefined, club: undefined, points: undefined, position:3 },
          { index: 8, id:undefined, name: undefined, club: undefined, points: undefined, position:3 },
          { index: 9, id:undefined, name: undefined, club: undefined, points: undefined, position:3 },
          { index: 10, id:undefined, name: undefined, club: undefined, points: undefined, position:3 },
      ],
      benched: [{ index: 11, id:undefined, name: undefined, club: undefined, points: undefined, position:3 }]
  },
  strikers: {
      starter: [
          { index: 12, id:undefined, name: undefined, club: undefined, points: undefined, position:4 },
          { index: 13, id:undefined, name: undefined, club: undefined, points: undefined, position:4 },
      ],
      benched: [{ index: 14, id:undefined, name: undefined, club: undefined, points: undefined, position:4 },]
  }
}

function PlayerCard({player, includedPlayers=[], disabledPlayers, setPlayersList, setSelectionDetails}){
  const [isOpen, setIsOpen] = useState(false)
  function handleClick(e){
    if (e.target.id === 'modal-overlay') return setIsOpen(false)
    return setIsOpen(true)
  }
  function addPlayer(){
    let a
    if (player.position === 0) a = 'goalkeepers'
    else if(player.position === 1) a = 'defenders'
    else if(player.position === 3) a = 'midfielders'
    else if(player.position === 4) a = 'strikers'
    const reIndex = disabledPlayers[player.position].shift()

    setPlayersList(prev => {
      return {
        ...prev,
        [a]: {
          starter: prev[a].starter.map(item => (item.index === reIndex ? { ...item, id: player.id, name: player.last_name ? player.last_name : player.first_name, club: player.team__name, points: 14, position: player.position, price:player.price } : item)),
          benched: prev[a].benched.map(item => (item.index === reIndex ? { ...item, id: player.id, name: player.last_name ? player.last_name : player.first_name, club: player.team__name, points: 14, position: player.position, price:player.price } : item))
        }
      };
    });
    setSelectionDetails(prev => ({
      ...prev, ['money']:prev.money - player.price,
               ['players']:prev.players + 1
    }))
  }

  return(
      <Tr className='d-flex'>
        <Td className={`f-basis-70 ${includedPlayers[0].indexOf(player.id) !== -1 ? 'backgroundColor-red': ''}`}>
          <InvisibleButton className={'width-100 d-flex f-di-column'} onClick={handleClick}>
          <img src={`/src/assets/${player.team__name}-shirt.webp`} alt="" style={{width:'1rem'}}/>
          {player.last_name ?
            <p>{player.last_name}</p>
            :
            <p>{player.first_name}</p>
          }
          <p>{player.position}</p>
          <Modal isOpen={isOpen} className={'d-flex f-di-column gap-1 p-1'}>
            {includedPlayers[1][player.position] >= CONDITION[player.position] &&
              <p>you have exceded this positon</p>
            }
            <Button childern='' onClick={addPlayer}>add player</Button>
            <Button childern=''>player information</Button>
          </Modal>
          </InvisibleButton>
        </Td>
        <Td className='f-basis-30'>
          {player.price}
        </Td>
      </Tr>
  )
}

function TransfersFilters({includedPlayers, disabledPlayers, setPlayersList, setSelectionDetails}){
  const [page, setPage] = useState(1)
  const [filters, setFilters] = useState()
  const {data, isLoading} = useGetPlayersFanstasy({team:filters?.team, position:filters?.position, sort:filters?.sort, page})
  if (isLoading) return null
  return(
    <div>
        <PlayerSelectionFilter filters={data?.filters} setFilters={setFilters}/>
        {Object.keys(data?.players).map(section => {
          return <div>
                  <SectionHeader>{section}</SectionHeader>
                  <table className='width-100 cap'>
                    <Thead>
                      <Tr>
                        <Th></Th>
                        <Th></Th>
                      </Tr>
                    </Thead>
                    <Tbody>
                      {data?.players[section].map(player => {
                        return <PlayerCard player={player} includedPlayers={includedPlayers} disabledPlayers={disabledPlayers} setPlayersList={setPlayersList} setSelectionDetails={setSelectionDetails}/>
                      })}
                    </Tbody>
                  </table>
              </div>
            })}
            <PageSlider page={page} setPages={setPage} pages={data?.page.num_of_pages} next={data?.page.next} prev={data?.page.prev}/>
      </div>
  )
}

function TeamSelection() {
  const [playersList, setPlayersList] = useState(AA)
  const [disabledPlayers, setDisabledPlayers] = useState({0:[0, 1], 1:[2, 3, 4, 5, 6], 3:[7, 8, 9, 10, 11], 4:[12, 13, 14]})
  const [selectionDetails, setSelectionDetails] = useState({money:100.00, players:0})

  const includedPlayers = useMemo(() => {
    const playerArr = Object.values(playersList).flatMap(({ starter, benched }) => [...starter, ...benched]);
    const a = playerArr.filter(player => disabledPlayers[player.position].indexOf(player.index) === -1)
    const teamsCount = a.reduce((acc, curr) => {
      acc[curr.club] = (acc[curr.club] || 0) + 1;
      return acc
    },{})
    const plus3Teams = Object.keys(teamsCount).filter(x => teamsCount[x] > 3);
    return [a.flatMap(player => player.id), (a.reduce((acc, curr) => {
      acc[curr.position] = (acc[curr.position] || 0) + 1;
      return acc
      },[])),
      plus3Teams]
  },[playersList, {...disabledPlayers}])

  useEffect(() => {
    console.log(playersList)
  },[playersList])

  function togglePitchPlayer(restore, position, index, price){
    if (restore){
      setDisabledPlayers(prev => ({...prev, [position]:prev[position].filter(x => x !== index).sort((a,b) => a - b)}))
      setSelectionDetails(prev => ({...prev, ['money']:prev['money'] - price, ['players']:prev['players'] + 1}))
    }
    else{
      let a
      if (position === 0) a = 'goalkeepers'
      else if(position === 1) a = 'defenders'
      else if(position === 3) a = 'midfielders'
      else if(position === 4) a = 'strikers'
      setDisabledPlayers(prev => ({...prev, [position]:[...prev[position], index].sort((a,b) => a-b)}))
      setSelectionDetails(prev => ({...prev, ['money']:prev.money + price, ['players']:prev.players - 1}))
      setPlayersList(prev => {
        return {
          ...prev,
          [a]: {
            starter: prev[a].starter.map(item => (item.index === index ? { ...item, index:index , id: undefined, name: undefined, club: undefined, points: undefined, position: position, price:undefined } : item)),
            benched: prev[a].benched.map(item => (item.index === index ? { ...item, index:index , id: undefined, name: undefined, club: undefined, points: undefined, position: position, price:undefined } : item))
          }
        };
      });
    }
  }

  function reset(){
    setPlayersList(AA);
    setDisabledPlayers({0:[0, 1], 1:[2, 3, 4, 5, 6], 3:[7, 8, 9, 10, 11], 4:[12 ,13 ,14]});
    setSelectionDetails({money:100.00, players:0})
  }

  function makeTransfers(){
    
  }
  function team3Plus(team){
    if (includedPlayers[2].indexOf(team) === -1) return false
    return true
  }

  return (
    <section className='fantasy-layout_with-side-bar'>
      <div>
        <TeamSelectionPitch playersList={playersList} reset={reset} disabledPlayers={disabledPlayers} setDisapledPlayers={setDisabledPlayers} selectionDetails={selectionDetails} togglePitchPlayer={togglePitchPlayer} team3Plus={team3Plus}/>
        fixtures
      </div>
      <TransfersFilters includedPlayers={includedPlayers} disabledPlayers={disabledPlayers} setPlayersList={setPlayersList} setSelectionDetails={setSelectionDetails}/>
    </section>
  )
}

export default TeamSelection