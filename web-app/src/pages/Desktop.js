import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Navbar from '../components/Navbar';

import Dashboard from './Dashboard';
import Observations from './Observations';
import Battle from './Battle';


function Desktop(props) {

  return (
    <div className="desktop-container">
      <Router>
        <Navbar username={props.username} profile_pic={props.profile_pic} collaspe={true}/>
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