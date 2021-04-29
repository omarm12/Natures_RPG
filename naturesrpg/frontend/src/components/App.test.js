import React from "react";
import { shallow, mount } from "enzyme";
import App from "./App";

it("Renders without crashing", () => {
  shallow(<App />);
});

it("Renders Observations header", () => {
  const wrapper = shallow(<App />);
  const app = <h1 style={{ paddingBottom: "20px", paddingTop: "60px", paddingLeft: "10px"}}>Observations</h1>;
  const loading = <div>Loading...</div>;
  expect(wrapper.contains(app) || wrapper.contains(loading)).toEqual(true);
});

it("Renders loading state", () => {
  const wrapper = shallow(<App />);
  const app = <div className="Observation" style={{ paddingBottom: "30px"}}></div>;
  const loading = <div>Loading...</div>;
  expect(wrapper.contains(loading)).toEqual(true);
});