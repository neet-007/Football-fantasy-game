import { useRef } from 'react'
import './Select.css'

function Option({lable='label', value}){
    return (
        <option value={value ? value : lable}>{lable}</option>
    )
}

function Select({options=['label', 'aaaa'], filter ,setValue=() => {}}) {
  const ref = useRef()
  console.log(ref.current?.value)
  return (
    <>
    {
      filter ?
      (filter === 'team' || filter === 'position') ?
      <select className='select_select' onChange={(e) => setValue(prev => ({...prev, [filter]:e.target.value}))}ref={ref}>
        {options.map(option => {
          return <Option lable={option[1]} value={option[0]}/>
        })}
      </select>
      :
      <select className='select_select' onChange={(e) => setValue(prev => ({...prev, [filter]:e.target.value}))}ref={ref}>
        {options.map(option => {
          return <Option lable={option}/>
        })}
      </select>
      :
      <select className='select_select' onChange={(e) => setValue(e.target.value)}ref={ref}>
        {options.map(option => {
          return <Option lable={option}/>
        })}
      </select>
    }
    </>
  )
}

export default Select