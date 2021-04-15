import React from "react";
import { shallow, mount } from "enzyme";
import App from "./App";
import LoadingIcon from './components/img/catLoadingIcon.gif'
import Observations from './components/Observations'
import GetObsdata from './components/getObsdata'

it("Renders without crashing", () => {
  shallow(<App />);
});

it("Renders Observations header", () => {
  const wrapper = shallow(<App />);
  const app = <h1 style={{ paddingBottom: "20px", paddingTop: "60px", paddingLeft: "10px"}}>Observations</h1>;
  const loading = <div>
  <img className="loading" src={LoadingIcon} alt="Loading..."/>
</div>;
  expect(wrapper.contains(app) || wrapper.contains(loading)).toEqual(true);
});

it("Renders loading state", () => {
  const wrapper = shallow(<App />);
  const app = <div className="Observation" style={{ paddingBottom: "30px"}}></div>;
  const loading = <div>
  <img className="loading" src={LoadingIcon} alt="Loading..."/>
</div>;
  expect(wrapper.contains(loading)).toEqual(true);
});

it("Renders eduLink button", () => {
  const wrapper = shallow(<GetObsdata />);
  const eduLink = <button className="eduLink">Click to learn more information</button>
  expect(wrapper.contains(eduLink)).toEqual(true);
})

it("Renders popup", () => {
  const wrapper = shallow(<Observations trigger={true}/>);
  const health = <h5>Health: 100</h5>;
  expect(wrapper.contains(health)).toEqual(true);
})