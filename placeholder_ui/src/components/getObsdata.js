import React, { useState, useEffect } from 'react'
import './getObsdata.css'
import axios from 'axios'
// import loading from './img/catLoadingIcon.gif'

function GetObsdata(props) {

    return (
        <div>
            <a href={props.wiki} target="_blank" rel="noreferrer">
                <button className="eduLink">
                    Click to learn more information
                </button>
            </a>
        </div>
    )
  }
  
  export default GetObsdata;