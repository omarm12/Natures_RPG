import {
    Card,
    CardBody,
    Progress
  } from "shards-react";
import React, { Component } from 'react'
import ReactRoundedImage from "react-rounded-image";

export default class ObservationBattleCard extends Component {

    

    render() {

        const getBarColor = function (maxHealth, curHealth) {

            if(curHealth > maxHealth * 0.5){
                return "success";
            } else if(curHealth > maxHealth * 0.2){
                return "warning";
            }
            return "danger";
        }
    
        let barColor = getBarColor(this.props.startHealth || this.props.health || 100, this.props.health || 100);

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
                    <div>{this.props.health || "100"} hp / {this.props.startHealth || this.props.health || "100"} hp</div>
                    <Progress theme={barColor} value={this.props.health || "100"} max={this.props.startHealth || this.props.health || "100"}/>
                </CardBody>
            </Card>
        )
    }
}

