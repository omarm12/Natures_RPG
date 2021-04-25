import React from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import './App.css'

import Login from './pages/login'
import Start from './pages/startingScreen'
import Home from './pages/home'

function App() {

  return (
    <Router>
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/home">
            <Home />
          </Route>
          <Route path="/">
            <Start />
          </Route>
        </Switch>
    </Router>
  )
}

export default App