import React, {useState, useEffect, useMemo} from 'react'
import Thead from '../../../components/shared/Thead/Thead'
import Tbody from '../../../components/shared/Tbody/Tbody'
import Tr from '../../../components/shared/Tr/Tr'
import Th from '../../../components/shared/Th/Th'
import Td from '../../../components/shared/Td/Td'
import Modal from '../../../components/shared/Modal/Modal'
import Button from '../../../components/shared/Button/Button'
import InvisibleButton from '../../../components/shared/InvisibleButton/InvisibleButton'
import PlayerSelectionFilter from '../../../components/PlayerSelectionFilter/PlayerSelectionFilter'
import PlayerTransferPitch from '../../../components/PlayerTransferPitch/PlayerTransferPitch'
import PageSlider from '../../../components/PageSlider/PageSlider'
import SectionHeader from '../../../components/shared/SectionHeader/SectionHeader'
import { useGetPlayersFanstasy, useGetUserTeam } from '../../../lib/queriesAndMutaions'

const CONDITION = {
  0:2,
  1:5,
  3:5,
  4:3
}

const AA = {
  goalkeepers: {
      starter: [{ index: 0, id:2, name: 'alissson', club: 'liverpool', points: 11, position:0 }],
      benched: [{ index: 1, id:38, name: 'edenrson', club: 'liverpool', points: 11, position:0 }]
  },
  defenders: {
      starter: [
          { index: 2, id:5, name: 'arnoled', club: 'liverpool', points: 11, position:1 },
          { index: 3, id:205, name: 'trpieer', club: 'liverpool', points: 11, position:1 },
          { index: 4, id:139, name: 'cash', club: 'liverpool', points: 11, position:1 },
          { index: 5, id:67, name: 'saliba', club: 'liverpool', points: 11, position:1 }
      ],
      benched: [{ index: 6, id:41, name: 'guihe', club: 'liverpool', points: 11, position:1 }]
  },
  midfielders: {
      starter: [
          { index: 7, id:3, name: 'salah', club: 'liverpool', points: 11, position:3 },
          { index: 8, id:44, name: 'deburin', club: 'liverpool', points: 11, position:3 },
          { index: 9, id:69, name: 'saka', club: 'liverpool', points: 11, position:3 },
          { index: 10, id:70, name: 'odegard', club: 'liverpool', points: 11, position:3 }
      ],
      benched: [{ index: 11, id:65, name: 'rashford', club: 'liverpool', points: 11, position:3 }]
  },
  strikers: {
      starter: [
          { index: 12, id:54, name: 'haaland', club: 'liverpool', points: 11, position:4 },
          { index: 13, id:16, name: 'houjland', club: 'liverpool', points: 11, position:4 }
      ],
      benched: [{ index: 14, id:1, name: 'watkins', club: 'liverpool', points: 11, position:4 }]
  }
}

function PlayerCard({player, includedPlayers=[], disabledPlayers, setPlayersList, setTransferDetails, togglePitchPlayer}){
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
          starter: prev[a].starter.map(item => (item.index === reIndex ? { ...item, id: player.id, name: player.last_name ? player.last_name : player.first_name, club: player.team__name, points: 14, position: player.position } : item)),
          benched: prev[a].benched.map(item => (item.index === reIndex ? { ...item, id: player.id, name: player.last_name ? player.last_name : player.first_name, club: player.team__name, points: 14, position: player.position } : item))
        }
      };
    });
    togglePitchPlayer(false, false, player, reIndex);
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

function TransfersFilters({includedPlayers, disabledPlayers, setPlayersList, setTransferDetails, togglePitchPlayer}){
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
                        return <PlayerCard player={player} includedPlayers={includedPlayers} disabledPlayers={disabledPlayers} setPlayersList={setPlayersList} setTransferDetails={setTransferDetails} togglePitchPlayer={togglePitchPlayer}/>
                      })}
                    </Tbody>
                  </table>
              </div>
            })}
            <PageSlider page={page} setPages={setPage} pages={data?.page.num_of_pages} next={data?.page.next} prev={data?.page.prev}/>
      </div>
  )
}

function Transferss({userTeam}) {
  const [playersList, setPlayersList] = useState(userTeam.players)
  const [disabledPlayers, setDisabledPlayers] = useState({0:[], 1:[], 3:[], 4:[]})
  const [wildCard, setWildCard] = useState(false)
  const [transferDetails, setTransferDetails] = useState({freeTransfers:userTeam.team.free_transfers, cost:0, moneyRemaining:parseFloat(userTeam.team.bank), playersTransferd:{}})

  const playersIst = useMemo(() => {
    const {captins, ...other} = playersList
    return Object.values(other).flatMap(({starter, benched}) => [...starter, ...benched]).map(x => x.id)
  })

  const includedPlayers = useMemo(() => {
    const {captins, ...other} = playersList
    const playerArr = Object.values(other).flatMap(({ starter, benched }) => [...starter, ...benched]);
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
    console.log(transferDetails)
  },[transferDetails])
  function togglePitchPlayer(restore, remove, player, index){
    if (restore){
      setDisabledPlayers(prev => ({...prev, [player.position]:prev[player.position].filter(x => x !== player.index).sort((a,b) => a - b)}))
      setTransferDetails(prev => ({...prev, ['moneyRemaining']:prev.moneyRemaining - player.price}))
    }
    else if(remove){
      console.log(!Object.keys(transferDetails.playersTransferd).find(x => x.includes(`${player.id}-${player.index}`)))
      setDisabledPlayers(prev => ({...prev, [player.position]:[...prev[player.position], player.index].sort((a,b) => a-b)}))
      setTransferDetails(prev => ({...prev,
        ['moneyRemaining']:prev.moneyRemaining + player.price,}))
    }
    // you need to get the prev player id instead of using player id
    else{
      setTransferDetails(prev => (
        !Object.keys(prev.playersTransferd).find(x => x.includes(`-${index}`)) ?
        {...prev, ['moneyRemaining']:prev.moneyRemaining - player.price,
                  ['cost']:prev.freeTransfers <= 0 ? prev.cost + 4 :prev.cost,
                  ['freeTransfers']:playersIst.includes(player.id) ? prev.freeTransfers:prev.freeTransfers <= 0 ? 0 : prev.freeTransfers - 1,
                  ['playersTransferd']:{...prev.playersTransferd,
                  [`${player.id}-${index}`]:[player.id, (wildCard || prev.freeTransfers > 0) ? 0 : 4]}
                }
        :
        {...prev, ['moneyRemaining']:prev.moneyRemaining - player.price,
                  ['playersTransferd']:Object.keys(prev.playersTransferd).reduce((acc, curr) => {
                    if(!curr.includes(`-${index}`)){
                      acc[curr] = prev.playersTransferd[curr]
                    }
                    return acc
                  },{[`${player.id}-${index}`]:[player.id, (wildCard || prev.freeTransfers > 0) ? 0 : 4]})
                }
      ));
    }
  }

  function reset(){
    setPlayersList(userTeam.players);
    setDisabledPlayers({0:[], 1:[], 3:[], 4:[]});
    setTransferDetails({freeTransfers:userTeam.team.free_transfers, cost:0, moneyRemaining:parseFloat(userTeam.team.bank), playersTransferd:{}})
  }

  function team3Plus(team){
    if (includedPlayers[2].indexOf(team) === -1) return false
    return true
  }
  return (
    <section className='fantasy-layout_with-side-bar'>
      <div>
        <PlayerTransferPitch transferDetails={transferDetails} setTransferDetails={setTransferDetails} playersList={playersList} reset={reset} disabledPlayers={disabledPlayers} togglePitchPlayer={togglePitchPlayer} team3Plus={team3Plus}/>
        fixtures
      </div>
      <TransfersFilters includedPlayers={includedPlayers} disabledPlayers={disabledPlayers} setPlayersList={setPlayersList} setTransferDetails={setTransferDetails} togglePitchPlayer={togglePitchPlayer}/>
    </section>
  )
}

function Transfers(){
  const {data, isLoading} = useGetUserTeam()
  if (isLoading) return null
  return(
    <Transferss userTeam={data}/>
  )
}

export default Transfers