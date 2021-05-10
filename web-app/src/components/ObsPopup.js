import {
    Card,
    CardImg,
    CardBody
  } from "shards-react";
import React from 'react'
import './ObsPopup.css'
import closeBtn from '../images/close.png'
import EduInfo from './EduInfo'

import { IoIosCloseCircleOutline } from "react-icons/io";

function Observations(props) {

    // if no comments were made for the observation, Comment is set to N/A
    var comment = props.comment

    if (comment === null) {
        comment = "N/A"
    }

    return (props.trigger) ? (
                    <div className="popup">
                        <Card className="popup-inner">
                            <CardBody>
                                <br /><br  />
                                <button className="close-btn" onClick={() => props.setTrigger(false)}>
                                    <IoIosCloseCircleOutline className="close-btn-icon"/>
                                </button>
                                {props.children}
                                <div className="text-center">
                                    <CardImg className="img" src={props.image} alt="" />
                                    <br /><br  />
                                    <h1>{props.name}</h1>
                                    <h4>Taxa name: {props.title}</h4>
                                    <p>Comment: {comment}</p>
                                    <h4>Stats:</h4>
                                    <h5>Health: 100</h5>
                                    <h5>Attack: 90</h5>
                                    <h5>Defense: 80</h5>
                                    <h5>Speed: 100</h5>
                                    <p>Observed on: {props.time}</p>
                                    <p>Quality: {props.quality}</p>
                                    <EduInfo wiki={props.wiki}/>
                                </div>
                            </CardBody>
                        </Card>
                    </div>
    ) : "";
}

export default Observations;
