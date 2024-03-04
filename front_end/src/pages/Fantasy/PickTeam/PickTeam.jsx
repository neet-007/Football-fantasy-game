import React, { useEffect, useMemo, useState } from 'react'
import TeamSideBar from '../../../components/TeamSideBar/TeamSideBar'
import PlayerPickPitch from '../../../components/PlayerPickPitch/PlayerPickPitch'
import { useGetUserTeam } from '../../../lib/queriesAndMutaions'

function PickTeamm({userTeam}) {
  const [playersList, setPlayersList] = useState(userTeam.players)
  const [selectedPlayer, setSelectedPlayer] = useState(undefined)

  const positionsCounts = useMemo(() => {
    const {captins, ...other} = playersList
    const a = Object.values(other).flatMap(({starter, benched}) => [...starter]).reduce((acc, curr) => {
      if (curr.position !== 2){
        acc[curr.position] = (acc[curr.position] || 0) + 1;
      }
      return acc
    },[]);
    const a1 = 3 < a[1] && a[1]< 5
    const a3 = 2 < a[3] && a[3]< 5
    const a4 = 1 < a[4] && a[4]< 3
    return [
      [true, false, null, false, false],
      [false, a1, null,a1 && a3,a1 && a4],
      null,
      [false, a3 && a1, null, a3, a3 && a4],
      [false, a4 && a1, null, a4 && a3, a4]
    ]
  },[playersList])

  useEffect(() => {
    console.log(playersList)
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

  function toggleTeamSwitch({player, benched, cancel}){
    if (cancel){
      setSelectedPlayer(undefined)
      return
    }

    if (selectedPlayer){
    let a, b;
    if (player.position === 0) a = 'goalkeepers'
    if (player.position === 1) a = 'defenders'
    if (player.position === 3) a = 'midfielders'
    if (player.position === 4) a = 'strikers'

    if (selectedPlayer[1] === 0) b = 'goalkeepers'
    if (selectedPlayer[1] === 1) b = 'defenders'
    if (selectedPlayer[1] === 3) b = 'midfielders'
    if (selectedPlayer[1] === 4) b = 'strikers'

    const selectedPlayerObj = playersList[b][selectedPlayer[2] ? 'benched':'starter'].find(x => x.index === selectedPlayer[0])

    if (player.benched_order && selectedPlayer[2]){
      setPlayersList(prev => ({
        ...prev,
        [a]:{
          starter:prev[a].starter,
          benched:prev[a].benched.map(x => x.index === player.index ? {...x, benched_order:selectedPlayerObj.benched_order}:x)
        },
        [b]:{
          starter:prev[b].starter,
          benched:prev[b].benched.map(x => x.index === selectedPlayer[0] ? {...x, benched_order:player.benched_order}:x)
        }
      }))
    }
    else if(selectedPlayer[2]){
      if (a === b){
        setPlayersList(prev => ({
          ...prev,
          [a]:{starter:prev[a].starter.filter(x => x.index !== player.index).concat([{...selectedPlayerObj, benched_order:null, captin:player.captin, vice_captin:player.vice_captin}]),
              benched:prev[a].benched.filter(x => x.index !== selectedPlayer[0]).concat([{...player, benched_order:selectedPlayerObj.benched_order, captin:selectedPlayerObj.captin, vice_captin:selectedPlayerObj.vice_captin}])},
          ['captins']:{captin: prev.captins.captin === player.id ? selectedPlayerObj.id:prev.captins.captin,
                       vice_captin: prev.captins.vice_captin === player.id ? selectedPlayerObj.id: prev.captins.vice_captin}
        }))
      }
      else{
      setPlayersList(prev => ({
        ...prev,
        [a]:{starter:prev[a].starter.filter(x => x.index !== player.index),
            benched:prev[a].benched.concat([{...player, benched_order:selectedPlayerObj.benched_order, captin:selectedPlayerObj.captin, vice_captin:selectedPlayerObj.vice_captin}])},
        [b]:{starter:prev[b].starter.concat([{...selectedPlayerObj, benched_order:null, captin:player.captin, vice_captin:player.vice_captin}]),
            benched:prev[b].benched.filter(x => x.index !== selectedPlayer[0])
        },
        ['captins']:{captin: prev.captins.captin === player.id ? selectedPlayerObj.id : prev.captins.captin,
                    vice_captin: prev.captins.vice_captin === player.id ? selectedPlayerObj.id : prev.captins.vice_captin}
      }))
    }
    }
    else{
      if (a === b){
        setPlayersList(prev => ({
          ...prev,
          [a]:{starter:prev[a].starter.filter(x => x.index !== selectedPlayer[0]).concat([{...player, benched_order:null, captin:selectedPlayerObj.captin, vice_captin:selectedPlayerObj.vice_captin}]),
              benched:prev[a].benched.filter(x => x.index !== player.index).concat([{...selectedPlayerObj, benched_order:player.benched_order, captin:player.captin, vice_captin:player.vice_captin}])},
          ['captins']:{captin:prev.captins.captin === selectedPlayerObj.id ? player.id : prev.captins.captin,
                      vice_captin:prev.captins.vice_captin === selectedPlayerObj.id ? player.id : prev.captins.vice_captin}
            }))
      }
      else{
      setPlayersList(prev => ({
        ...prev,
        [a]:{starter:prev[a].starter.concat([{...player, benched_order:null, captin:selectedPlayerObj.captin, vice_captin:selectedPlayerObj.vice_captin}]),
            benched:prev[a].benched.filter(x => x.index !== player.index)},
        [b]:{starter:prev[b].starter.filter(x => x.index !== selectedPlayer[0]),
            benched:prev[b].benched.concat([{...selectedPlayerObj, benched_order:player.benched_order, captin:player.captin, vice_captin:player.vice_captin}])
        },
        ['captins']:{captin:prev.captins.captin === selectedPlayerObj.id ? player.id : prev.captins.captin,
                     vice_captin:prev.captins.captin === selectedPlayerObj.id ? player.id : prev.captins.vice_captin}
      }))
    }
  }
    setSelectedPlayer(undefined)
    return
  }

  setSelectedPlayer([player.index, player.position, benched])
  }
  return (
    <section className='fantasy-layout_with-side-bar cap'>
      <div>
        <p>pick team - team</p>
        <PlayerPickPitch playersList={playersList} selectedPlayer={selectedPlayer} setSelectedPlayer={setSelectedPlayer} positionsCounts={positionsCounts} togglePickTeam={togglePickTeam} toggleTeamSwitch={toggleTeamSwitch}/>
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