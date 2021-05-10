import React from 'react';
import ReactRoundedImage from "react-rounded-image";

import "./ProfileCard.css";

function ProfileCard(props) {
  return (
    <div id="profile-card">
        <div className="profile-image">
            <ReactRoundedImage
                image={props.image}
                roundedColor="rgba(36, 36, 36, .2)"
                imageWidth="85"
                imageHeight="85"
                roundedSize="8"
                borderRadius="70"
            />
        </div>
        <div className="profile-username">{props.username}</div>
    </div>
  );
}

export default ProfileCard;