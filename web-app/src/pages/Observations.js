import {
  Card
} from "shards-react";
import { Container, Row, Col} from "shards-react";
import React, {useState, useEffect} from "react";

import axios from 'axios'

import './Observations.css';
import ObsPopup from '../components/ObsPopup'
import { ButtonDropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import { Textfit } from 'react-textfit';
import PuffLoader from "react-spinners/PuffLoader";

const player_url = "http://127.0.0.1:8000/info/players/"
const observations_url = "http://127.0.0.1:8000/info/obs/"

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

const sortOptions = ["Order Observed", "Taxa", "Stats", "Quality", "A-Z", "HP", "Attack", "Level", "Reverse"];

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const userid = urlParams.get('u');


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
                </CardBody>
            </Card>
          </div>
      </button>
      <ObsPopup 
        trigger={buttonPopup} 
        setTrigger={setButtonPopup}
        name={props.name}
        title={props.title}
        image={props.image}
        hp={props.hp}
        attack={props.attack}
        defense={props.defense}
        evasion={props.evasion}
        accuracy={props.accuracy}
        speed={props.speed}
        xp={props.xp}
        level={props.level}
        conf={props.conf}
        m1={props.m1}
        m2={props.m2}
        m3={props.m3}
        m4={props.m4}
        quality={props.quality}
        wiki={props.wiki}
        >
      </ObsPopup>
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
  const [username, setUsername] = useState("username");

  const [wow, setWow] = useState(false);
  const toggleWow = () => setWow(!wow);

  const toggle = () => setOpen(!dropdownOpen);

  useEffect(() => {
    // //Order Observed
    // if (sortOption === sortOptions[0]) {
    //   items.sort((a, b) => (a.created_at > b.created_at) ? -1 : 1)
    // }
    //Taxa alphabetical
    if (sortOption === sortOptions[1]) {
      items.sort((a, b) => (a.taxa > b.taxa) ? 1 : -1)
    }
    else if (sortOption === sortOptions[3]) {
      items.sort((a, b) => (a.quality > b.quality) ? -1 : 1)
    }
    else if (sortOption === sortOptions[4]) {
      items.sort((a, b) => (a.name > b.name) ? 1 : -1)
    }
    else if (sortOption === sortOptions[5]) {
      items.sort((a, b) => (a.hp > b.hp) ? -1 : 1)
    }
    else if (sortOption === sortOptions[6]) {
      items.sort((a, b) => (a.attack > b.attack) ? -1 : 1)
    }
    else if (sortOption === sortOptions[7]) {
      items.sort((a, b) => (a.level > b.level) ? -1 : 1)
    }
    //reverse
    else {
      items.reverse()
    }

    toggleWow();

  }, [sortOption])

  useEffect(() => {

    async function fetchData() {
      console.log(userid)
      const request = await axios.get(observations_url + userid + '/');
      const requestName = await axios.get(player_url + userid + '/');
      console.log(request)
      console.log(requestName.data.username)
      setItems(request.data)
      setUsername(requestName.data.username)
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
          key={observation.obs_id}
          name={observation.name}
          title={observation.taxa}
          image={convertToLarge(observation.image_link)}
          hp={observation.hp}
          attack={observation.attack}
          defense={observation.defense}
          evasion={observation.evasion}
          accuracy={observation.accuracy}
          speed={observation.speed}
          xp={observation.total_xp}
          level={observation.level}
          conf={observation.num_of_confirmations}
          m1={observations.move_1}
          m2={observations.move_2}
          m3={observations.move_3}
          m4={observations.move_4}
          quality={observation.quality}
          wiki={observation.wiki_link}
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
              {/* <DropdownItem onClick={() => setSort(sortOptions[0])}>{sortOptions[0]}</DropdownItem> */}
              <DropdownItem onClick={() => setSort(sortOptions[1])}>{sortOptions[1]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[2])}>{sortOptions[2]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[3])}>{sortOptions[3]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[4])}>{sortOptions[4]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[5])}>{sortOptions[5]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[6])}>{sortOptions[6]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[7])}>{sortOptions[7]}</DropdownItem>
              <DropdownItem onClick={() => setSort(sortOptions[8])}>{sortOptions[8]}</DropdownItem>

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
