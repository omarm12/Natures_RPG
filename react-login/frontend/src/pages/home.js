import React from 'react'

function home() {

    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const username = urlParams.get('username');

    return <h1>Welcome back, {username}</h1>
}

export default home
