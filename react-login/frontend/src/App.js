import React from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css'
import { Container, Row, Col} from "shards-react";

function App() {

  function Start() {
    return(
      <Container className="login-btn">
        <Row>
          <Col>
            <a href="/login">
              <button  id="loginbtn" className="btn">Login</button>
            </a>
          </Col>
        </Row>
      </Container>
    )
  }

  //redirect to login
  function Login() {
    window.location = "http://localhost:9000/login/iNat"
    return <></>
  }

  function Home() {

    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const username = urlParams.get('username');

    return (
      <h1>Welcome back, {username}</h1>
    )
  }

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