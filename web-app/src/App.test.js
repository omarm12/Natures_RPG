import React from "react";
import { shallow, mount } from "enzyme";
import App from "./App";

it("Renders without crashing, yay ╮(＾▽＾)╭", () => {
  shallow(<App />);
});