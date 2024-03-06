import './Select.css'

function Option({lable='label', value}){
    return (
        <option value={value !== undefined ? value : lable}>{lable}</option>
    )
}

function Select({options=['label', 'aaaa'], filter , value, setValue=() => {}}) {
  /*
  const [a, setA] = useState()
  console.log(a)
  function handleChange(e){
    setA(e.target.value)
    setValue(prev => ({...prev, [filter]:e.target.value}))
  }*/
  return (
    <>
    {
      filter ?
      (filter === 'team' || filter === 'position' || filter === 'status') ?
      <select className='select_select' onChange={(e) => setValue(prev => ({...prev, [filter]:e.target.value}))} value={value}>
        {options.map(option => {
          return <Option lable={option[1]} value={option[0]}/>
        })}
      </select>
      :
      <select className='select_select' onChange={(e) => setValue(prev => ({...prev, [filter]:e.target.value}))} value={value}>
        {options.map(option => {
          return <Option lable={option}/>
        })}
      </select>
      :
      <select className='select_select' onChange={(e) => setValue(e.target.value)} value={value}>
        {options.map(option => {
          return <Option lable={option}/>
        })}
      </select>
    }
    </>
  )
}

export default Select