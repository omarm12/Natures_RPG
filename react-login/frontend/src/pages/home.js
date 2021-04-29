import React from 'react'
import axios from 'axios'

const player_url = "http://127.0.0.1:8000/players/"
const observations_url = "http://127.0.0.1:8000/obs/"

// create and add player to Django
async function newUser(id, username, numObs) {
  const res = await axios.post(player_url, {
    iNat_user_id: id,
    username: username,
    num_of_obs: numObs
  })
  console.log(res)

  // if (numObs > 0) {
    addObservations(username, id, numObs)
  // }
}

// get observaitions
async function addObservations(username, id, numObs) {

  async function fetchData() {
      const request = await axios.get("https://api.inaturalist.org/v1/observations/?page=1&per_page=100&user_id=" + username);
      console.log(request.data.results)

      const observations = request.data.results

      let name
      let title
      let image
      let body
      let quality
      let comment
      let time
      let wiki
      let observation_id
      let numConfirmations

      for (let i = 0; i < observations.length; i++) {
        name=observations[i].species_guess
        title=observations[i].taxon.name
        image = observations[i].photos[0].url
        body=observations[i].place_guess
        quality=observations[i].quality_grade
        comment=observations[i].description
        time=observations[i].observed_on_string
        wiki=observations[i].taxon.wikipedia_url
        observation_id = observations[i].id
        numConfirmations = observations[i].identifications_count

        const res = await axios.post(observations_url + id + '/', {
          owner:{    
            iNat_user_id: id,
            username: username,
            num_of_obs: numObs},
          obs_id: observation_id,
          name:name,
          taxa:title,
          num_of_confirmations:numConfirmations,
        })
      }

    }
  fetchData()

}

// check Django for user
async function getUser(id, username, numObs) {

  let apiRes = null;
  try {
      apiRes = await axios.get(player_url + id + '/');
      console.log(apiRes.data)
  }
  catch (err) {
      console.error("Error response:");
      console.error(err.response.data);    // ***
      console.error(err.response.status);  // ***
      console.error(err.response.headers); // ***
      console.log("Player not registered")
      newUser(id, username, numObs)
    } finally {
      console.log(apiRes);
    }
}

function home() {

    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const username = urlParams.get('username');
    const id = urlParams.get('id')
    const numObs = urlParams.get('count')
    getUser(id, username, numObs)

    return <h1>Welcome back, {username}</h1>
}

export default home
