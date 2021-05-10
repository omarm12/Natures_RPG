import {
  Card
} from "shards-react";
import { Container, Row, Col} from "shards-react";
import React, {useState, useEffect} from "react";

import axios from 'axios'

import './Observations.css';
import Observations from '../components/ObsPopup'
import { ButtonDropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import { Textfit } from 'react-textfit';
import PuffLoader from "react-spinners/PuffLoader";

// Sample observations for testing
const sampleObservationList = [
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=1", description:"Description", key:1},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=2", description:"Description", key:2},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=3", description:"Description", key:3},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=4", description:"Description", key:4},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=5", description:"Description", key:5},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=6", description:"Description", key:6},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=7", description:"Description", key:7},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=8", description:"Description", key:8},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=9", description:"Description", key:9},
  {title:"Observation Name", name:"name", image:"https://loremflickr.com/300/200/wildlife?random=10", description:"Description", key:10}
];

const sortOptions = ["Order Observed", "Taxa", "Stats", "Quality", "A-Z", "Reverse"];

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const username = urlParams.get('username');

// Observation component
// This is a basic component that gets populated with data
// to be used in the list of observations

function Observation(props) {

  const [buttonPopup, setButtonPopup] = useState(false);
  return (
    <Col sm="6" md="4" lg="3">
      <button className="btn" onClick={() => setButtonPopup(true)}>
        <div className="Observation" style={{ paddingBottom: "30px"}}>
            <Card>
                <CardImg src={props.image} top="true" />
                <CardBody>
                  <CardTitle>{props.name}</CardTitle>
                  <p>{props.title}</p>
                  <p>{props.body}</p>
                </CardBody>
            </Card>
          </div>
      </button>
      <Observations 
        trigger={buttonPopup} 
        setTrigger={setButtonPopup}
        image={props.image}
        name={props.name}
        title={props.title}
        body={props.body}
        quality={props.quality}
        comment={props.comment}
        time={props.time}
        wiki={props.wiki}
        >
      </Observations>
    </Col>
  );
}

function convertToLarge(url){
  var position = url.search("square");
  if(position !== -1){
    return url.substring(0, position) + "large" + url.substring(position + 6);
  } else {
    return url;
  }
}

// Essentially the app in its entirety, returning JSX to be rendered in the browser
function Observations() {

  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);
  const [dropdownOpen, setOpen] = useState(false);
  const [sortOption, setSort] = useState(sortOptions[0]);

  const [wow, setWow] = useState(false);
  const toggleWow = () => setWow(!wow);

  const toggle = () => setOpen(!dropdownOpen);

  useEffect(() => {
    //Order Observed
    if (sortOption === sortOptions[0]) {
      items.sort((a, b) => (a.created_at > b.created_at) ? -1 : 1)
    }
    //Taxa alphabetical
    else if (sortOption === sortOptions[1]) {
      items.sort((a, b) => (a.taxon.name > b.taxon.name) ? 1 : -1)
    }
    else if (sortOption === sortOptions[3]) {
      items.sort((a, b) => (a.quality_grade > b.quality_grade) ? -1 : 1)
    }
    else if (sortOption === sortOptions[4]) {
      items.sort((a, b) => (a.species_guess > b.species_guess) ? 1 : -1)
    }
    //reverse
    else {
      items.reverse()
    }

    toggleWow();

  }, [sortOption])

  useEffect(() => {

    async function fetchData() {

      const request = await axios.get("https://api.inaturalist.org/v1/observations/?page=1&per_page=100&user_id=" + username);
      console.log(request.data.results)
      setItems(request.data.results)
      setIsLoaded(true)
    }
    fetchData()

  }, [])

  // Error State
  if(error){
    return <div>Error: {error.message}</div>;
  } 
  // Loading State
  else if (!isLoaded) {
    return (
      <div className="loader">
        <div className="loader-icon">
          <PuffLoader color={"rgb(58, 134, 255, 1)"} size={80} />
        </div>
      </div>
    );
  } 
  // Loaded State
  else {
    var observations = <div></div>;
    var displayName = "Username";

    // Loads sample data into the observations variable if no username is provided
    if(u_id === null || items === 0){
      observations = sampleObservationList.map((observation) =>
        <Observation
          key={observation.key}
          name={observation.species_guess}
          title={observation.title}
          image={observation.image}
          body={observation.description}
        />
      );
      
    // Loads user observation data into the observations variable
    } else {

      observations = items.map((observation) =>
        <Observation
          key={observation.key}
          name={observation.species_guess}
          title={observation.taxon.name}
          image={convertToLarge(observation.photos[0].url)}
          body={observation.place_guess}
          quality={observation.quality_grade}
          comment={observation.description}
          time={observation.observed_on_string}
          wiki={observation.taxon.wikipedia_url}
        />
      ); 
      displayName = username;
    }  
    
    return (
      <div id="observations">
        <Container className="container" style={{ paddingBottom: "20px"}}>
          {/* Observations Heading */}
          <Row>
            <Col sm="12" md="12" lg="6" xl="6">
              <h1 className="observations-header">Observations</h1>
            </Col>
            <Col sm="12" md="12" lg="6" xl="6">
              <div className="observation-sort">
                <div className="observation-sort-drop">
                  <ButtonDropdown isOpen={dropdownOpen} toggle={toggle} className="dropDown">
                    <DropdownToggle caret color="white" lassName="dropDown-button">
                      {sortOption}
                    </DropdownToggle>
                    <DropdownMenu>
                      <DropdownItem onClick={() => setSort(sortOptions[0])}>{sortOptions[0]}</DropdownItem>
                      <DropdownItem onClick={() => setSort(sortOptions[1])}>{sortOptions[1]}</DropdownItem>
                      <DropdownItem onClick={() => setSort(sortOptions[2])}>{sortOptions[2]}</DropdownItem>
                      <DropdownItem onClick={() => setSort(sortOptions[3])}>{sortOptions[3]}</DropdownItem>
                      <DropdownItem onClick={() => setSort(sortOptions[4])}>{sortOptions[4]}</DropdownItem>
                      <DropdownItem onClick={() => setSort(sortOptions[5])}>{sortOptions[5]}</DropdownItem>
                    </DropdownMenu>
                  </ButtonDropdown>
                </div>
              </div>
            </Col>
          </Row>

          <ButtonDropdown isOpen={dropdownOpen} toggle={toggle} className="dropDown">
            <DropdownToggle caret className="dropDown-button">
              {sortOption}
            </DropdownToggle>
            <DropdownMenu>
              <DropdownItem onClick={() => setSort(sortOptions[0])}>{sortOptions[0]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[1])}>{sortOptions[1]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[2])}>{sortOptions[2]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[3])}>{sortOptions[3]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[4])}>{sortOptions[4]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[5])}>{sortOptions[5]}</DropdownItem>
            </DropdownMenu>
          </ButtonDropdown>
          <br /><br />
          {/* <Sort 
            sort={sortOption}
            data={observations}
            items={setItems}/> */}

          {/* Observation Cards */}
          <Row className="observation-row">{observations}</Row>
        </Container>
      </div>
    );
  }
}

// I don't know what this does but im too scared to delete it
export default Observations;
