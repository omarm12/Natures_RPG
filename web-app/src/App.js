import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import { Container, Row, Col} from "shards-react";

import Dashboard from './pages/Dashboard';
import Observations from './pages/Observations';
import Battle from './pages/Battle';

import Mobile from './pages/Mobile';
import Tablet from './pages/Tablet';
import Desktop from './pages/Desktop';
import {Responsive} from './components/Responsive';



function App() {
  return (

    <>
      <Responsive displayIn={["Mobile"]}>
        <Mobile/>
      </Responsive>
      {/*
      <Responsive displayIn={["Tablet"]}>
        <Tablet/>
      </Responsive>
      */}
      <Responsive displayIn={["Tablet", "Laptop"]}>
        <Desktop/>
      </Responsive>
    </>

  );
}

export default App;