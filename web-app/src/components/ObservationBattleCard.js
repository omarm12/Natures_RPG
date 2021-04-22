import {
    Card,
    CardTitle,
    CardImg,
    CardBody,
    Button
  } from "shards-react";
import React, { Component } from 'react'
import ReactRoundedImage from "react-rounded-image";

export default class ObservationBattleCard extends Component {

    constructor(props){
        super(props);
    }

    render() {
        return (
            <Card className="battle-observation-card">
                <CardBody>
                    <div className="observation-battle-image">
                        <ReactRoundedImage
                            image={this.props.image || "https://loremflickr.com/300/200/cat?random=1"}
                            roundedColor="rgba(36, 36, 36, .2)"
                            imageWidth="100"
                            imageHeight="100"
                            roundedSize="8"
                            borderRadius="70"
                        />
                    </div>
                    <div>{this.props.name || "Observation Name"}</div>
                    <div>Level {this.props.level || "1"}</div>
                    <div>{this.props.health || "100"} hp</div>
                </CardBody>
            </Card>
        )
    }
}

