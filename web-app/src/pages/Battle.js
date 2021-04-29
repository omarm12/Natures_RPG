import {
  Card,
  CardBody,
  Button
} from "shards-react";
import { Container, Row, Col} from "shards-react";
import React from "react";
import "./Battle.css";
import ObservationBattleCard from '../components/ObservationBattleCard';

function getMovetext(value){
  if(value === -2){
    return "Please select an option";
  } else if(value === -1){
    return "So... you would like to leave the match";
  } else if(value === 0){
    return "Switching to another observation I see...";
  } 
  return "You have chosen move " + value;
}

class Battle extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      action: -2,
      inBattle: false
    }
  }

  toggleBattle() {

    

    this.setState(state => {
      return {inBattle: !this.state.inBattle}
    })
  }

  moveSelect(value) {
    this.setState(state => {
      return {action: value}
    })
  }

  // Need to be further implemented, but rn it logs basic info to console
  sumbitMove(value){
    this.setState(state => {
      return {action: -2}
    })
    if(value === -2){
      console.log("No move was selected");
      return
    }
    console.log("Move submitted was " + value);
  }

  render(){

    if(!this.state.inBattle){
      return (
        <div className="startBattleBox">
          <Button className="startBattleButton" block theme="primary" size="lg" onClick={() => this.toggleBattle()}>Battle vs AI</Button>
          <Button block disabled theme="secondary" size="lg" onClick={() => this.toggleBattle()}>Battle vs Player</Button>
        </div>
      );
    }
    else { 
      return (
        <div id='battle'>
          <Container>
            <Row>
              <Col sm="12" md="6">
                <div className="observation-card">
                  <ObservationBattleCard startHealth="150" health="110" level="12" name="Jules the cat" image="https://loremflickr.com/300/200/wildlife?random=1"/>
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
                  <Button block theme="danger" onClick={() => this.toggleBattle()}>Leave</Button>
                </div>
              </Col>
              <Col sm="4">
                <div className="battle-button">
                  <Button block theme="info" onClick={() => this.moveSelect(1)} >Move 1</Button>
                </div>
              </Col>
              <Col sm="4">
                <div className="battle-button">
                  <Button block theme="info" onClick={() => this.moveSelect(2)}>Move 2</Button>
                </div>
              </Col>
            </Row>
            <Row>
              <Col sm="4">
                <div className="battle-button">
                  <Button block theme="secondary" onClick={() => this.moveSelect(0)}>Switch</Button>
                </div>
              </Col>
              <Col sm="4">
                <div className="battle-button">
                  <Button block theme="info" onClick={() => this.moveSelect(3)}>Move 3</Button>
                </div>
              </Col>
              <Col sm="4">
                <div className="battle-button">
                  <Button block theme="info" onClick={() => this.moveSelect(4)}>Move 4</Button>
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
  }

export default Battle;