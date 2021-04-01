/*
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

*/

import React from "react";
import { shallow, mount } from "enzyme";
import App from "./App";

it("renders without crashing", () => {
  shallow(<App />);
});

it("renders Observations header", () => {
  const wrapper = shallow(<App />);
  const welcome = <h1 style={{ paddingBottom: "20px", paddingTop: "60px", paddingLeft: "10px"}}>Observations</h1>;
  expect(wrapper.contains(welcome)).toEqual(true);
});
