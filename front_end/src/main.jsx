import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'
import { MainContextProvider } from './context/MainContext.jsx'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const qr = new QueryClient()

ReactDOM.createRoot(document.getElementById('root')).render(
  <QueryClientProvider client={qr}>
    <BrowserRouter>
      <MainContextProvider>
        <React.StrictMode>
            <App />
        </React.StrictMode>,
      </MainContextProvider>
  </BrowserRouter>
  </QueryClientProvider>
)
