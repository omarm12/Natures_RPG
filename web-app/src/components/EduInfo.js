import React from 'react'
import './EduInfo.css'

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