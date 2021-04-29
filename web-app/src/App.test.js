import React from "react";
import { shallow, mount } from "enzyme";
import App from "./App";

it("Renders without crashing, yay ╮(＾▽＾)╭", () => {
  shallow(<App />);
});

it("Renders Navbar", () => {
  const wrapper = shallow(<App />);
  const app = <h1 style={{ paddingBottom: "20px", paddingTop: "60px", paddingLeft: "10px"}}>Observations</h1>;
  expect(wrapper.contains(app)).toEqual(true);
});

it("Renders loading state", () => {
  const wrapper = shallow(<App />);
  const loading = <div>Loading...</div>;
  expect(wrapper.contains(loading)).toEqual(true);
});