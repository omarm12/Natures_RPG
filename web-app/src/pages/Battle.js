import {
  Card,
  CardTitle,
  CardImg,
  CardBody,
  Button
} from "shards-react";
import { Container, Row, Col} from "shards-react";
import React, { useEffect, useState } from "react";
import "./Battle.css";
import ObservationBattleCard from '../components/ObservationBattleCard';

function getMovetext(value){
  if(value == -2){
    return "Please select an option";
  } else if(value == -1){
    return "So... you would like to leave the match";
  } else if(value == 0){
    return "Switching to another observation I see...";
  } 
  return "You have chosen move " + value;
}

class Battle extends React.Component {

  constructor(props){
    super(props);
    this.state={action: -2}
  }

  handleClick(value) {
    this.setState(state => {
      return {action: value}
    })
  }

  // Need to be further implemented, but rn it logs basic info to console
  sumbitMove(value){
    this.setState(state => {
      return {action: -2}
    })
    if(value == -2){
      console.log("No move was selected");
      return
    }
    console.log("Move submitted was " + value);
  }

  render(){
  return (
    <div id='battle'>
      <Container>
        <Row>
          <Col sm="12" md="6">
            <div className="observation-card">
              <ObservationBattleCard health="120" level="12" name="Jules the cat" image="https://loremflickr.com/300/200/wildlife?random=1"/>
            </div>
          </Col>
          <Col sm="12" md="6">
            <div className="observation-card">
              <ObservationBattleCard />
            </div>
          </Col>
        </Row>
        <Row>
          <Col sm="4">
            <div className="battle-button">
              <Button block theme="danger" onClick={() => this.handleClick(-1)}>Leave</Button>
            </div>
          </Col>
          <Col sm="4">
            <div className="battle-button">
              <Button block theme="info" onClick={() => this.handleClick(1)} >Move 1</Button>
            </div>
          </Col>
          <Col sm="4">
            <div className="battle-button">
              <Button block theme="info" onClick={() => this.handleClick(2)}>Move 2</Button>
            </div>
          </Col>
        </Row>
        <Row>
          <Col sm="4">
            <div className="battle-button">
              <Button block theme="secondary" onClick={() => this.handleClick(0)}>Switch</Button>
            </div>
          </Col>
          <Col sm="4">
            <div className="battle-button">
              <Button block theme="info" onClick={() => this.handleClick(3)}>Move 3</Button>
            </div>
          </Col>
          <Col sm="4">
            <div className="battle-button">
              <Button block theme="info" onClick={() => this.handleClick(4)}>Move 4</Button>
            </div>
          </Col>
        </Row>
        <Row>
          <div className="battle-textbox">
            <Card>
              <CardBody>
                {getMovetext(this.state.action)}
              </CardBody>
            </Card>
          </div>
        </Row>
        <Row>
          <Col sm="3">
            <div className="battle-button">
              <Button block theme="success" onClick={() => this.sumbitMove(this.state.action)}>Submit</Button>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
  }
}

export default Battle;