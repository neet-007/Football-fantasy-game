import React, { useRef } from 'react'
import Select from '../../../components/shared/Select/Select'
import Button from '../../../components/shared/Button/Button'
import { usePostLeagueClassic } from '../../../lib/queriesAndMutaions'

function CreateLeagueClassic() {
  const {mutateAsync:postLeagueClassic} = usePostLeagueClassic()
  const nameRef = useRef()
  const gameWeekRef = useRef()
  function handleSubmit(e){
    e.preventDefault()
    postLeagueClassic({name:nameRef.current.value, startingGameWeek:1})
  }
  return (
    <section>
        <h3>
            create invitational league and cup
        </h3>
        <form onSubmit={handleSubmit}>
            <span>
                <label htmlFor="create-league-classic-name">league name</label>
                <input type="text" name="create-league-classic-name" id="create-league-classic-name" maxLength={30}
                       ref={nameRef}/>
            </span>
            <Select options={Array.from({length: 38}, (_, index) => "Gameweek " + (index + 1))}/>
            <Button childern='' type='submit'>create</Button>
        </form>
    </section>
  )
}

export default CreateLeagueClassic