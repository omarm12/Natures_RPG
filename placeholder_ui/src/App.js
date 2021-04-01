import {
  Card,
  CardTitle,
  CardImg,
  CardBody
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
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=7", description:"Description", key:7},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=8", description:"Description", key:8},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=9", description:"Description", key:9},
  {title:"Observation Name", image:"https://loremflickr.com/300/200/wildlife?random=10", description:"Description", key:10}
];

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const username = urlParams.get('username');

// Observation component
// This is a basic component that gets populated with data
// to be used in the list of observations
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


// Essentially the app in its entirety, returning JSX to be rendered in the browser
function App() {

  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  
  useEffect(() => {

    // Fetches data from url + username
    fetch("https://api.inaturalist.org/v1/observations/?page=1&per_page=100&user_id=" + username)
      .then(res => res.json())
      .then(

        // We got our data
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },

        // Error handling
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])

  // Error State
  if(error){
    return <div>Error: {error.message}</div>;
  } 
  // Loading State
  else if (!isLoaded) {
    return <div>Loading...</div>;
  } 
  // Loaded State
  else {
    var observations = <div></div>;
    var displayName = "Username";

    // Loads sample data into the observations variable if no username is provided
    if(username == null || items == 0){
      observations = sampleObservationList.map((observation) =>
        <Observation
          key={observation.key}
          title={observation.title}
          image={observation.image}
          body={observation.description}
        />
      );
      
    // Loads user observation data into the observations variable
    } else {
      console.log(items.results);
      observations = items.results.map(observation =>
        <Observation
          key={observation.key}
          title={observation.taxon.name}
          image={observation.photos[0].url}
          body={observation.place_guess}
        />
      ); 
      displayName = username;
    }  

    return (
      <div className="App">
        <Container className="dr-example-container"  style={{ paddingBottom: "20px"}}>

          {/* User Heading */}
          <Row>
            <h1 style={{ paddingBottom: "20px", paddingTop: "40px", paddingLeft: "10px"}}>User</h1>
          </Row>

          {/* User Card */}
          <Row>
            <Col sm="6" md="4" lg="4">
              <Card>
                <CardBody style={{marginTop: "10px"}}>

                  {/* displayName is set to "Username" until data is successfully retrived from api */}
                  <CardTitle>{displayName}</CardTitle>
                </CardBody>
              </Card>
            </Col>
          </Row>

          {/* Observations Heading */}
          <Row>
            <h1 style={{ paddingBottom: "20px", paddingTop: "60px", paddingLeft: "10px"}}>Observations</h1>
          </Row>

          {/* Observation Cards */}
          <Row>{observations}</Row>
        </Container>
      </div>
    );
  }
}

// I don't know what this does but im too scared to delete it
export default App;