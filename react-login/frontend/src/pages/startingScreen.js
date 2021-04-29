import React from 'react'
import { Container, Row, Col} from "shards-react";

function startingScreen() {
    return (
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

export default startingScreen