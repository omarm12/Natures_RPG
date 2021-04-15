import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Navbar from './components/Navbar';

import Dashboard from './pages/Dashboard';
import Observations from './pages/Observations';
import Battle from './pages/Battle';

function Desktop() {
  return (
    <div className="desktop-container">
      <Router>
        <Navbar collaspe={false}/>
        <div className="desktop-body">
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