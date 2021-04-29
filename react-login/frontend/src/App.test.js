//import { render, screen } from '@testing-library/react';
import { render, unmountComponentAtNode } from "react-dom";
import { act } from 'react-dom/test-utils';
import { MemoryRouter } from "react-router-dom";
import App from './App';

it("navigates to login after clicking button", async => {
  // in a real test a renderer like "@testing-library/react"
  // would take care of setting up the DOM elements
  const root = document.createElement('div');
  document.body.appendChild(root);

  // Render app
  render(
    <MemoryRouter initialEntries={['/']}>
      <App />
    </MemoryRouter>,
    root
  );

  // Interact with page
  act(() => {
    // Find the link (perhaps using the text content)
    const loginLink = document.querySelector('a');
    // Click it
    loginLink.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  });

  const site = window.location.href

  // Check correct page content showed up
  expect(site).toBe('https://www.inaturalist.org/users/sign_in');
});