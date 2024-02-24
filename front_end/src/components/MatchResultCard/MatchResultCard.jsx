import React from 'react'
import './MatchResultCard.css'
import ResultBox from './ResultBox/ResultBox'
import {ArrowRight} from 'react-bootstrap-icons'
import {useNavigate} from 'react-router-dom'
import TimeBox from './TimeBox/TimeBox'
import Button from '../shared/Button/Button'

function MatchResultCard({matchTime=90, homeTeam='HomeTeam', awayTeam='AwayTeam', time, homeResults, awayResults}) {
  const navigate = () => {}
  return (
    <article className={`main-theme_match-result-card match-result-card_article d-flex align-items-center justify-content-center gap-1`}>
        <span>
            {matchTime}
        </span>
        <div className={` d-flex gap-1`}>
            <span>
                {homeTeam}
            </span>
         </div>
        {time ?
            <TimeBox/>
        :
            <ResultBox homeResults={homeResults} awayResults={awayResults}/>
        }
        <div className={` d-flex gap-1`}>
            <span>
                {awayTeam}
            </span>
         </div>
        <div className='m-left-auto'>
            staduim
        </div>
        {time &&
            <Button backgroundColor={'backgroundColor-white'}/>
        }
        <span className='d-flex align-items-center justify-content-center cursor-pointer m-left-auto'
              onClick={() => navigate(-1)}>
            <ArrowRight/>
        </span>
    </article>
  )
}

export default MatchResultCard