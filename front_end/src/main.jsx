import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'
import { MainContextProvider } from './context/MainContext.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <MainContextProvider>
      <React.StrictMode>
          <App />
      </React.StrictMode>,
    </MainContextProvider>
  </BrowserRouter>
)
