import React, { useState, useEffect } from 'react'
import './getObsdata.css'
import axios from 'axios'
import loading from './img/catLoadingIcon.gif'

function GetObsdata() {
    const url = "https://api.inaturalist.org/v1/observations/70860013"
    const [obsData, setObsData] = useState(null)

    let content = 
        <div className="loading">
            <img src={loading} alt=""/>
            <h1>Loading...</h1>
        </div>

    useEffect(() => {
        axios.get(url)
            .then(response => 
            {
                setObsData(response.data.results[0].community_taxon.wikipedia_url)
                console.log({response})
            })
    }, [url])

    if(obsData)
    {
        content = 
        <div>
            <a href={obsData} target="_blank" rel="noreferrer">
                <button className="eduLink">
                    Click to learn more information
                </button>
            </a>
        </div>
    }

    return (
        <div>{content}</div>
    )

  }
  
  export default GetObsdata;