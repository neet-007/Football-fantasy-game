import React from 'react'
import Button from '../../../components/shared/Button/Button'
import { useNavigate } from 'react-router-dom'

function CreateLeague() {
  const navigate = useNavigate()
  return (
    <section>
        <h3>
            choose a league type to create
        </h3>
        <div>
            <h4>
                classic league
            </h4>
            <p>
                In a league with classic scoring, teams are ranked based on their total points in the game. You can join or leave a league with classic scoring at any point during the season.
            </p>
            <Button childern='' onClick={() => navigate('classic')}>
                create league
            </Button>
        </div>
        <div>
            <h4>
                head 2 head league
            </h4>
            <p>
            In a league with head-to-head scoring, every team plays a match against another team in the league each Round. The match result is based on the Round score of each team minus any transfer points spent preparing for the Round.

            The Head-to-Head schedule is generated at the start of the league's first Round. Once the schedule has been generated the league is locked and teams will not be able to join or leave.
            </p>
            <Button childern='' onClick={() => navigate('head-2-head')}>
                create head 2 head league
            </Button>
        </div>
    </section>
  )
}

export default CreateLeague