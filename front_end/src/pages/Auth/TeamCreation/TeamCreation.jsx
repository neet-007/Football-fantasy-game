import React, { useRef } from 'react'
import { useGetPremierLeagueBaseTeams, usePostTeamCreation } from '../../../lib/queriesAndMutaions'
import Button from '../../../components/shared/Button/Button'
import { redirect } from 'react-router-dom'

function TeamCreation() {
  const {data, isLoading, isError, error} = useGetPremierLeagueBaseTeams()
  const {mutateAsync:postTeamCreation} = usePostTeamCreation()
  const nameRef = useRef()
  const teamRef = useRef([])

  if(isError){
    console.log(error)
    return <h1>ERROR</h1>
  }
  if (isLoading) return <h1>LOADING....</h1>

  function handleSubmit(e) {
    e.preventDefault()
    postTeamCreation({name:nameRef.current.value, favoriteTeamPk:teamRef.current}).then(res => {
        if (res.error){
            return <h1>Error</h1>
        }
        redirect('/fantasy/team-selection')

    })
  }
  return (
    <form className='auth-layout_form cap' onSubmit={handleSubmit}>
        <span className='d-flex f-di-column'>
            <label htmlFor='team-name' >team name</label>
            <input id='team-name' type="text" className='auth-layout_form-input' ref={nameRef}/>
        </span>
        <span>
            <h3>favorite team</h3>
            <div className='d-flex f-di-column'>{data?.map(team => {
                return <span key={`check-box_team-${team.team_code}`}className='f-basis-50'>
                        <label htmlFor={`check-box_team-${team.team_code}`}>
                            {team.name}
                        </label>
                        <input id={`check-box_team-${team.team_code}`} type="checkbox" value={team.team_code} onChange={e => e.target.checked ? teamRef.current.push(team.team_code):null}/>
                       </span>
            })}</div>
        </span>
        <Button childern='' type='submit'>
            submit
        </Button>
    </form>
  )
}

export default TeamCreation