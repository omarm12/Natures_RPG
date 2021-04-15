import {
    Card,
    CardTitle,
    CardImg,
    CardBody
  } from "shards-react";
import React from 'react'
import './Observations.css'
import closeBtn from './img/close.png'
import { Container, Row, Col} from "shards-react";
import EduInfo from './getObsdata'

function Observations(props) {

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
                                        <p>Comment: {props.comment}</p>
                                        <h4>Stats:</h4>
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