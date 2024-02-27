import React from 'react'
import InvisibleButton from '../../components/shared/InvisibleButton/InvisibleButton'
import {ChevronDoubleLeft, ChevronDoubleRight, ChevronLeft, ChevronRight} from 'react-bootstrap-icons'
import './PageSlider.css'

function PageSlider({page, pages, next, prev, setPages}) {
  return (
    <div className='d-flex justify-content-between align-items-center p-1'>
        <InvisibleButton className={`page-slider_button ${prev === -1 ? 'page-slider_button-disabled':''}`} onClick={prev !== -1 ? () => setPages(1) : () => {}}>
            <ChevronDoubleLeft/>
        </InvisibleButton>
        <div className='d-flex justify-content-between f-basis-30 align-items-center gap-1'>
            <InvisibleButton className={`page-slider_button ${prev === -1 ? 'page-slider_button-disabled':''}`} onClick={prev !== -1 ? () => setPages(page - 1) : () => {}}>
                <ChevronLeft/>
            </InvisibleButton>
            <div>
                <span>{page}</span>
                <span>of</span>
                <span>{pages}</span>
            </div>
            <InvisibleButton className={`page-slider_button ${next == -1 ? 'page-slider_button-disabled':''}`} onClick={next !== -1 ? () => setPages(page + 1) : () => {}}>
                <ChevronRight/>
            </InvisibleButton>
        </div>
        <InvisibleButton className={`page-slider_button ${next == -1 ? 'page-slider_button-disabled':''}`} onClick={next !== -1 ? () => setPages(pages) : () => {}}>
            <ChevronDoubleRight/>
        </InvisibleButton>
    </div>
  )
}

export default PageSlider