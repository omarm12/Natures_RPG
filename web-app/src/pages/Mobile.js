import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Navbar from '../components/Navbar';

import Dashboard from './Dashboard';
import Observations from './Observations';
import Battle from './Battle';

function Desktop() {
  return (

    <div className="desktop-container">
      
      <Router>
        <Navbar/>
        <div className="desktop-body">
          <div style={{color: "#ff0000", position: 'absolute', right:"10px", top:"5px"}}>The mobile version isn't complete</div>
          <Switch >
            <Route path='/' exact component={Dashboard} />
            <Route path='/observations' component={Observations} />
            <Route path='/battle' component={Battle} />
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default Desktop;