import {Routes, Route} from 'react-router-dom'
import './App.css'
import InfoLayout from './pages/Info/InfoLayout'
import FantasyLayout from './pages/Fantasy/FantasyLayout'
import Home from './pages/Info/Home/Home'
import Fixtures from './pages/Info/Fixtures/Fixtures'
import Results from './pages/Info/Results/Results'
import Stats from './pages/Info/Stats/Stats'
import Tables from './pages/Info/Tables/Tables'

function App() {
  return (
    <>
      <Routes>
        <Route element={<InfoLayout/>}>
          <Route path='' element={<Home/>}/>
          <Route path='/fixtures' element={<Fixtures/>}/>
          <Route path='/results' element={<Results/>}/>
          <Route path='/stats' element={<Stats/>}/>
          <Route path='/tables' element={<Tables/>}/>
        </Route>
        <Route path='/auth'>

        </Route>
        <Route path='/fantasy' element={<FantasyLayout/>}>

        </Route>
      </Routes>
    </>
  )
}

export default App
