import React from "react";
import "./Welcome.css";
import { Button } from "shards-react";

function Welcome(){

  
  return (
    <div id="welcome-wrapper"> 
      <div className="welcome-text-wrapper">
        <div className="welcome-signin">
          <a href="info/login">
            <Button outline pill size="lg" theme="success">Sign In</Button>
          </a>
        </div>
        <div className="welcome-text">
          <div className="welcome-header-text">
            Welcome to <br/> Nature's RPG
          </div>
          <div className="welcome-body">
            <div className="welcome-line1">
              A place to interact with and battle wildlife <span className="bold">you</span> have observed
            </div>
            <div className="welcome-line2">
            Sign in to your iNaturalist account to get started
            </div>
          </div>
        </div>
      </div>
      
    </div>
  );
}

export default Welcome;