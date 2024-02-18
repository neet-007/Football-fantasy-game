import './Select.css'

function Option({lable='label', value}){
    return (
        <option value={value ? value : lable}>{lable}</option>
    )
}

function Select({options=['label', 'aaaa'], setValue=() => {}}) {
  return (
    <select className='select_select' onChange={(e) => setValue(e.target.value)}>
        {options.map(option => {
          return <Option lable={option}/>
        })}
    </select>
  )
}

export default Select