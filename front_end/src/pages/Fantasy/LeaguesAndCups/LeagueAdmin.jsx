import React, { useRef } from 'react'
import Select from '../../../components/shared/Select/Select'
import Button from '../../../components/shared/Button/Button'
import { useParams } from 'react-router-dom'
import { useGetLeagueStandings } from '../../../lib/queriesAndMutaions'

function LeagueAdmin() {
  const {id} = useParams()
  const {data, isLoading} = useGetLeagueStandings({id})

  const LeagueDetailsRef = useRef()

  function handleSubmit(e){
    e.preventDefault()
    const temp = LeagueDetailsRef.current.children
    console.log(temp[1].children[1].value)
    console.log(temp[2].value)
    console.log(temp[3].value)
    console.log(temp[4].value)
  }

  function handleSuspenseSearch(e){
    if(e.key === ' ' && e.target.value !== ''){
        console.log(e.target.value)
    }
  }

  function handleAdminSearch(e){
    if(e.key === ' ' && e.target.value !== ''){
        console.log(e.target.value)
    }
  }
  if (isLoading) return null
  return (
    <section>
        <form ref={LeagueDetailsRef} onSubmit={handleSubmit}>
            <div>
                <p>league code</p>
                <Button childern=''>dasd</Button>
            </div>
            <h3>league details</h3>
            <span>
                <label htmlFor="">league name</label>
                <input type="text" name="" id="" defaultValue={data?.name}/>
            </span>
            <Select/>
            <Select/>
            <input type="checkbox" value={'sad'}/>
            <Button childern='' type='submit'>aa</Button>
        </form>
        <div>
            <h3>add league suspension</h3>
            <p></p>
            <div>
                <input type="search" onKeyUp={handleSuspenseSearch}/>
                <Button childern=''>dasd</Button>
            </div>
        </div>
        <div>
            <h3>change league admins</h3>
            <div>
                <input type="search" onKeyUp={handleAdminSearch}/>
                <Button childern=''>dasd</Button>
            </div>
        </div>
        <div>
            <h3>delete league</h3>
            <p></p>
            <Button childern=''>dsada</Button>
        </div>
    </section>
  )
}

export default LeagueAdmin