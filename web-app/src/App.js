import './App.css';
import Mobile from './pages/Mobile';
import Desktop from './pages/Desktop';
import Welcome from './pages/Welcome';
import React, {useState, useEffect} from "react";
import {Responsive} from './components/Responsive';



function App() {

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const u_id = urlParams.get('u');

  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("https://api.inaturalist.org/v1/users/" + u_id)
      .then(res => res.json())
      .then(
        (result) => {
          setItems(result);
          setIsLoaded(true);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setError(error);
          setIsLoaded(true);
        }
      )
  }, [])

  if (!u_id || error) {
    return <Welcome/>
  } else if (!isLoaded) {
    return <div>Loading...</div>;
  } else {

    const username = items.results[0].name;
    const profile_pic = items.results[0].icon_url;;

    return (
      <>
        <Responsive displayIn={["Mobile"]}>
          <Mobile/>
        </Responsive>
        {/*
        <Responsive displayIn={["Tablet"]}>
          <Tablet/>
        </Responsive>
        */}
        <Responsive displayIn={["Tablet", "Laptop"]}>
          <Desktop username={username} profile_pic={profile_pic}/>
        </Responsive>
      </>

    );
  }
}

export default App;
