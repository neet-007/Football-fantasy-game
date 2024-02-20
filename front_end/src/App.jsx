import './App.css'
import MatchResultCard from './components/MatchResultCard/MatchResultCard'
import Button from './components/shared/Button/Button'
import Select from './components/shared/Select/Select'
import Row from './components/shared/Row/Row'
import Column from './components/shared/Column/Column'
import LeagueTable from './components/LeagueTable/LeagueTable'
import Navbar from './components/Navbar/Navbar'
import FantasyNavbar from './components/FantasyNavbar/FantasyNavbar'
import PlayerSmallCard from './components/shared/PlayerSmallCard/PlayerSmallCard'
import PlayerCarousel from './components/PlayerCarousel/PlayerCarousel'
function App() {
  return (
    <>
      <Navbar/>
      <PlayerCarousel/>
    </>
  )
}

export default App
