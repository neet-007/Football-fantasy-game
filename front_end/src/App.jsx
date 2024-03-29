import {Routes, Route} from 'react-router-dom'
import { lazyLoad } from './utils/lazyLoad'
import './App.css'
import { Suspense } from 'react'
import FixturesAndResultsBase from './pages/Info/FixturesAndResultsBase/FixturesAndResultsBase'
import PlayerStats from './pages/Info/Stats/PlayerStats'

const InfoLayout = lazyLoad('../pages/Info/InfoLayout')
const Home = lazyLoad('../pages/Info/Home/Home')
const Fixtures = lazyLoad('../pages/Info/Fixtures/Fixtures')
const Results = lazyLoad( '../pages/Info/Results/Results')
const Stats = lazyLoad('../pages/Info/Stats/Stats')
const Tables = lazyLoad('../pages/Info/Tables/Tables')

const AuthLayout = lazyLoad('../pages/Auth/AuthLayout')
const SignUp = lazyLoad('../pages/Auth/SignUp/SignUp')
const Login = lazyLoad('../pages/Auth/Login/Login')
const TeamCreation = lazyLoad('../pages/Auth/TeamCreation/TeamCreation')

const FantasyLayout = lazyLoad('../pages/Fantasy/FantasyLayout')
const FantasyFixtures = lazyLoad('../pages/Fantasy/Fixtures/Fixtures')
const FantasyHome = lazyLoad('../pages/Fantasy/Home/Home')
const FantasyLeaguesAndCups = lazyLoad('../pages/Fantasy/LeaguesAndCups/LeaguesAndCups')
const FantasyLeagueAdmin = lazyLoad('../pages/Fantasy/LeaguesAndCups/LeagueAdmin')
const FantasyLeagueStandings = lazyLoad('../pages/Fantasy/LeaguesAndCups/LeagueStandings')
const FanstayCreateLeague = lazyLoad('../pages/Fantasy/LeaguesAndCups/CreateLeague')
const FanstayCreateLeagueClassic = lazyLoad('../pages/Fantasy/LeaguesAndCups/CreateLeagueClassic')
const FanstayCreateLeagueH2H = lazyLoad('../pages/Fantasy/LeaguesAndCups/CreateLeagueH2H')
const FantasyPickTeam = lazyLoad('../pages/Fantasy/PickTeam/PickTeam')
const FantasyTeamSelection = lazyLoad('../pages/Fantasy/TeamSelection/TeamSelection')
const FantasyPoints = lazyLoad('../pages/Fantasy/Points/Points')
const FantasyStats = lazyLoad('../pages/Fantasy/Stats/Stats')
const FanstayInjuries = lazyLoad('../pages/Fantasy/Injuries/Injuries')
const FantasyTransfers = lazyLoad('../pages/Fantasy/Transfers/Transfers')

function App() {
  return (
    <>
    <Suspense>
    <Routes>
        <Route path='' element={<InfoLayout/>}>
          <Route path='' element={<Home/>}/>
          <Route element={<FixturesAndResultsBase/>}>
            <Route path='/fixtures' element={<Fixtures/>}/>
            <Route path='/results' element={<Results/>}/>
          </Route>
          <Route path='/stats' element={<Stats/>}/>
          <Route path='/stats/player/:stat' element={<PlayerStats/>}/>
          <Route path='/tables' element={<Tables/>}/>
          <Route path='/fantasy' element={<FantasyLayout/>}>
            <Route path='' element={<FantasyHome/>}/>
            <Route path='fixtures' element={<FantasyFixtures/>}/>
            <Route path='leagues-and-cups' element={<FantasyLeaguesAndCups/>}/>
            <Route path='leagues-and-cups/:id/admin' element={<FantasyLeagueAdmin/>}/>
            <Route path='leagues-and-cups/:id/standings' element={<FantasyLeagueStandings/>}/>
            <Route path='leagues-and-cups/create-league' element={<FanstayCreateLeague/>}/>
            <Route path='leagues-and-cups/create-league/classic' element={<FanstayCreateLeagueClassic/>}/>
            <Route path='leagues-and-cups/create-league/head-2-head' element={<FanstayCreateLeagueH2H/>}/>
            <Route path='points' element={<FantasyPoints/>}/>
            <Route path='stats' element={<FantasyStats/>}/>
            <Route path='injuries' element={<FanstayInjuries/>}/>
            <Route path='pick-team' element={<FantasyPickTeam/>}/>
            <Route path='team-selection' element={<FantasyTeamSelection/>}/>
            <Route path='transfers' element={<FantasyTransfers/>}/>
          </Route>
        </Route>
        <Route element={<AuthLayout/>}>
          <Route path='/auth/signup' element={<SignUp/>}/>
          <Route path='/auth/login' element={<Login/>}/>
          <Route path='/auth/team-creation' element={<TeamCreation/>}/>
        </Route>
        <Route path='*' element={<h1>not found</h1>}/>
      </Routes>
    </Suspense>
    </>
  )
}

export default App
