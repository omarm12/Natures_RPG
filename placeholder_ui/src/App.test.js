import React from "react";
import { shallow, mount } from "enzyme";
import App from "./App";
import LoadingIcon from './components/img/catLoadingIcon.gif'
import Observations from './components/Observations'
import GetObsdata from './components/getObsdatas'

it("Renders without crashing", () => {
  shallow(<App />);
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
