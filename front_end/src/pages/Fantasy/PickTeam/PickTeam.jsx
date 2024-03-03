import React, { useEffect, useMemo, useState } from 'react'
import TeamSideBar from '../../../components/TeamSideBar/TeamSideBar'
import PlayerPickPitch from '../../../components/PlayerPickPitch/PlayerPickPitch'
import { useGetUserTeam } from '../../../lib/queriesAndMutaions'

function PickTeamm({userTeam}) {
  const [playersList, setPlayersList] = useState(userTeam.players)
  const [selectedPlayer, setSelectedPlayer] = useState(null)

  const positionsCounts = useMemo(() => {
    const {captins, ...other} = playersList
    const a = Object.values(other).flatMap(({starter, benched}) => [...starter]).reduce((acc, curr) => {
      acc[curr.position] = (acc[curr.position] || 0) + 1;
      return acc
    },{});
    const a1 = a[1] < 5
    const a3 = a[3] < 5
    const a4 = a[4] < 3
    return {
      0:{0:true, 1:false, 3:false, 4:false},
      1:{0:false, 1:a1, 3:a1 && a3, 4:a1 && a4},
      3:{0:false, 1:a3 && a1, 3:a3, 4:a3 && a4},
      4:{0:false, 1:a4 && a1, 3:a4 && a3, 4:a4}
    }
  },[playersList])

  function togglePickTeam(player, captin=false, viceCaptin=false){
    let a;
    if (player.position === 0) a = 'goalkeepers'
    if (player.position === 1) a = 'defenders'
    if (player.position === 3) a = 'midfielders'
    if (player.position === 4) a = 'strikers'
    setPlayersList(prev => ({
      ...prev,
      [a]: {
        starter: prev[a].starter.map(item => (item.id === player.id ? captin ? {...player, ['captin']:true} : item : viceCaptin ? {...player, ['vice_captin']:true} : item)),
        benched: prev[a].benched.map(item => (item.id === player.id ? captin ? {...player, ['captin']:true} : item : viceCaptin ? {...player, ['vice_captin']:true} : item))
      },
      ['captins']:captin ? {...prev.captins, ['captin']:player.id} : viceCaptin ? {...prev.captins, ['vice_captin']:player.id} : {...prev.captins}
    }))
  }
  return (
    <section className='fantasy-layout_with-side-bar cap'>
      <div>
        <p>pick team - team</p>
        <PlayerPickPitch playersList={playersList} togglePickTeam={togglePickTeam}/>
        results
      </div>
      <TeamSideBar userTeam={userTeam.team}/>
    </section>
  )
}

function PickTeam() {
  const {data, isLoading} = useGetUserTeam()
  if (isLoading) return null
  return(
    <PickTeamm userTeam={data}/>
  )
}

export default PickTeam