import {
  Card,
  CardHeader,
  CardTitle,
  CardImg,
  CardBody,
  CardFooter,
  CardSubtitle,
  Button
} from "shards-react";
import { Container, Row, Col} from "shards-react";
import React, { useEffect, useState } from "react";

// Sample observations for testing
const sampleObservationList = [
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=1", description:"Description", key:1},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=2", description:"Description", key:2},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=3", description:"Description", key:3},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=4", description:"Description", key:4},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=5", description:"Description", key:5},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=6", description:"Description", key:6},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=7", description:"Description", key:7}
];

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const username = urlParams.get('username');

//drmcmillan_bms


// Observation element
function Observation(props) {
  return (
    <Col sm="6" md="4" lg="3">
      <div className="Observation" style={{ paddingBottom: "30px"}}>
        <Card>
          <CardImg src={props.image} top="true"/>
          <CardBody>
            <CardTitle>{props.title}</CardTitle>
            <p>{props.body}</p>
          </CardBody>
        </Card>
      </div>
    </Col>
  );
}



function App() {

  // Takes in the observations, and maps them to a series of <Observation>
  
  /*
  var Observations = GetObservations().map((observation) =>
    <Observation
      key={observation.key}
      title={observation.title}
      image={observation.image}
      body={observation.description}
    />
  );  */

  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  // Note: the empty deps array [] means
  // this useEffect will run once
  // similar to componentDidMount()
  useEffect(() => {
    fetch("https://api.inaturalist.org/v1/observations/?page=1&per_page=100&user_id=" + username)
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])

  if(error){
    return <div>Error: {error.message}</div>;
  } else if (!isLoaded) {
    return <div>Loading...</div>;
  } else {

    //console.log(items.results);


    
    var Observations = <div></div>;
    
    if(items == 0){
      Observations = sampleObservationList.map((observation) =>
        <Observation
          key={observation.key}
          title={observation.title}
          image={observation.image}
          body={observation.description}
        />
      ); 
    } else {
      console.log(items);
      Observations = items.results.map(observation =>
        <Observation
          key={observation.key}
          title={observation.taxon.name}
          image={observation.photos[0].url}
          body={observation.place_guess}
        />
      ); 
    }  

    return (
      <div className="App">
        <Container className="dr-example-container"  style={{ paddingBottom: "20px"}}>
          <Row>
            <h1 style={{ paddingBottom: "20px", paddingTop: "40px", paddingLeft: "10px"}}>User</h1>
          </Row>
          <Row>
            <Col sm="6" md="4" lg="4">
              <Card>
                <CardBody style={{marginTop: "10px"}}>
                  <CardTitle>{username}</CardTitle>
                </CardBody>
              </Card>
            </Col>
          </Row>
          <Row>
            <h1 style={{ paddingBottom: "20px", paddingTop: "60px", paddingLeft: "10px"}}>Observations</h1>
          </Row>
          <Row>{Observations}</Row>
        </Container>
      </div>
    );
  }
}

export default App;