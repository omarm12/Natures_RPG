import {
    Card,
    CardImg,
    CardBody
  } from "shards-react";
import React from 'react'
import './ObsPopup.css'
import closeBtn from '../images/close.png'
import { Container, Row, Col} from "shards-react";
import EduInfo from './eduInfo'

function Observations(props) {

    // if no comments were made for the observation, Comment is set to N/A
    var comment = props.comment

    if (comment === null) {
        comment = "N/A"
    }

    return (props.trigger) ? (

        <Container className="Popup-container">
            <Row>
                <Col>
                    <div className="popup">
                        <div className="popup-inner">
                            <Card>
                                <CardBody>
                                    <br /><br  />
                                    <button className="close-btn" onClick={() => props.setTrigger(false)}>
                                        <CardImg width="35" height="35" src={closeBtn} alt="Close"/>
                                    </button>
                                    {props.children}
                                    <div className="text-center">
                                        <CardImg className="img" src={props.image} alt="" />
                                        <br /><br  />
                                        <h1>{props.name}</h1>
                                        <h4>Taxa name: {props.title}</h4>
                                        <h4>Stats:</h4>
                                        <h5>Health: {props.hp}</h5>
                                        <h5>Attack: {props.attack}</h5>
                                        <h5>Defense: {props.defense}</h5>
                                        <h5>Evasion: {props.evasion}</h5>
                                        <h5>Accuracy: {props.accuracy}</h5>
                                        <h5>Speed: {props.speed}</h5>
                                        <h5>Total XP: {props.xp}</h5>
                                        <h5>Level: {props.level}</h5><br></br>
                                        <h4>Moves:</h4>
                                        <h5>Move 1: {props.m1}</h5>
                                        <h5>Move 2: {props.m2}</h5>
                                        <h5>Move 3: {props.m3}</h5>
                                        <h5>Move 4: {props.m4}</h5>

                                        <p>Quality: {props.quality}</p>
                                        <EduInfo wiki={props.wiki}/>
                                    </div>
                                </CardBody>
                            </Card>
                        </div>
                    </div>
                </Col>
            </Row>
        </Container>
    ) : "";
}

export default Observations;
