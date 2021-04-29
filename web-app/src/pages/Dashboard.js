import React from 'react';
import { Card, CardBody, CardHeader, Col, Container, Row } from 'shards-react';
import "./Dashboard.css";
import { Textfit } from 'react-textfit';

import header_svg from "../images/header.svg";



function Dashboard() {
  return (
    <div id='dashboard'>
      <Container>
        <Row>
          <Col>
          <div className="dashboard-header">
            <div className="dashboard-header-text">
              <div className="dashboard-header-text-header">
                <Textfit mode="single">Welcome Back</Textfit>
              </div>
              <div className="dashboard-header-text-text">
                <Textfit mode="single">It looks like you have made <strong>2</strong> new </Textfit>
                <Textfit mode="single"> observations while you were gone.</Textfit>
              </div>
            </div>
            <img className="dashboard-header-image" src={header_svg} alt="Adventurous person" />
          </div>
          </Col>
        </Row>
        <Row>
          <Col sm="12" md="6" lg="6">
            <Card className="dashboard-card">
              <CardHeader>
                Card Title
              </CardHeader>
              <CardBody>
                Information
              </CardBody>
            </Card>
          </Col>
          <Col sm="12" md="6" lg="6">
            <Card className="dashboard-card">
              <CardHeader>
                Card Title
              </CardHeader>
              <CardBody>
                Information
              </CardBody>
            </Card>
          </Col>
          <Col sm="12" md="6" lg="6">
            <Card className="dashboard-card">
              <CardHeader>
                Card Title
              </CardHeader>
              <CardBody>
                Information
              </CardBody>
            </Card>
          </Col>
          <Col sm="12" md="6" lg="6">
            <Card className="dashboard-card">
              <CardHeader>
                Card Title
              </CardHeader>
              <CardBody>
                Information
              </CardBody>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Dashboard;