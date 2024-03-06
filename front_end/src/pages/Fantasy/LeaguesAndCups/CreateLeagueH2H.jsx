import React, { useRef } from 'react'
import Button from '../../../components/shared/Button/Button'
import Select from '../../../components/shared/Select/Select'
import { usePostLeagueH2H } from '../../../lib/queriesAndMutaions'

function CreateLeagueH2H() {
  const {mutateAsync:postLeagueH2H} = usePostLeagueH2H()
  const nameRef = useRef()
  function handleSubmit(e){
    e.preventDefault()
    postLeagueH2H({name:nameRef.current.value, startingGameWeek:1, isH2H:true, allowPostCreattionEntry:true})
  }
  return (
    <section>
        <h3>
            create head 2 head league and cup
        </h3>
        <form onSubmit={handleSubmit}>
            <span>
                <label htmlFor="create-league-classic-name">league name</label>
                <input type="text" name="create-league-classic-name" id="create-league-classic-name" maxLength={30}
                       ref={nameRef}/>
            </span>
            <Select options={Array.from({length: 38}, (_, index) => "Gameweek " + (index + 1))}/>
            <Button childern=''>create</Button>
        </form>
    </section>
  )
}

export default CreateLeagueH2H