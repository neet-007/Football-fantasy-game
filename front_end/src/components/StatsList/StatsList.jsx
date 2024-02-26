import React from 'react'
import './StatsList.css'
import Row from '../shared/Row/Row'
import Column from '../shared/Column/Column'
import Button from '../shared/Button/Button'
import { ArrowRight } from 'react-bootstrap-icons'

function StatsList({listName='name', list=[{name:'name', club:'club', number:2}, {name:'name', club:'club', number:2}]}) {
  return (
    <article className='stats-list_article'>
        <h3 className='stats-list_header'>{listName}</h3>
        <ul className='stats-list_ul'>
            <li className='stats-list_card'>
                <span className='stats-list_card-text'>
                    <p>1</p>
                    <p>{list[0].first_name}</p>
                    <p>{list[0].last_name}</p>
                    <p>{list[0].team__name}</p>
                    <p>{list[0][listName]}</p>
                </span>
                <p className='stats-list_card-img'>img</p>
            </li>
            {list.slice(1, 10).map((player, i) => {
                return <li>
                        <Row className={'d-flex gap-1'}>
                            <Column className={'stats-list_player-row-col-1'}>{i + 1}</Column>
                            <Column className={'stats-list_player-row-col-2'}>
                                <span>{player.team__name}</span>
                                <span>
                                    <p>{player.first_name}</p>
                                    <p>{player.last_name}</p>
                                    <p>{player.team__name}</p>
                                </span>
                            </Column >
                            <Column className={'stats-list_player-row-col-3'}>{player[listName]}</Column>
                        </Row>
                    </li>
            })}
            {list.length > 10 &&
             <li>
                 <Button className={'d-flex align-items-center justify-content-center gap-1 width-100'} childern=''
                         backgroundColor={'white'} noBorder>
                     <p>view full list</p>
                     <ArrowRight/>
                 </Button>
             </li>
            }
        </ul>
    </article>
  )
}

export default StatsList