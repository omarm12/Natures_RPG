import React from 'react';
import ReactDOM, { render } from 'react-dom';

//import './index.css';
import App from './components//App';
import reportWebVitals from './components/reportWebVitals';
import { Alert } from "shards-react";

const appDiv = document.getElementById("app");
render(<App />, appDiv);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
