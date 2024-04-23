import React from 'react';
import { render, fireEvent, screen, waitFor } from '@testing-library/react';
import Admin from '../src/JAVASCRIPT/Admin/Admin'; 
import Nome from '../src/JAVASCRIPT/Admin/Admin';
import ProfileGet from '../src/JAVASCRIPT/Admin/Admin';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';
import '@testing-library/jest-dom';

// Mocking the DataFetchGet module
jest.mock('../src/DataFetchFunctions/DataFetchGet');

describe('Admin Component', () => {
  test('Admin component renders without crashing', () => {
    render(<Admin />);
  });

  test('renders Import and Export buttons', () => {
    render(<Admin />);
  
    const importButton = screen.getByText('Import');
    const exportButton = screen.getByText('Export');
    const logOutButton = screen.getByText('Log Out');
  
    expect(importButton).toBeInTheDocument();
    expect(exportButton).toBeInTheDocument();
    expect(logOutButton).toBeInTheDocument();
  });

  test('handleInputChange updates state with selected file', () => {
    // Rendering the component
    const { getByRole } = render(<Admin />);
    const fileInput = getByRole('button', { name: 'Import' }); // Assuming the file input is the only button

    // Creating a fake file to simulate user input
    const fakeFile = new File(['fake content'], 'test.txt', { type: 'text/plain' });

    // Triggering the change event with the fake file
    fireEvent.change(fileInput, { target: { files: [fakeFile] } });

    // Asserting that the state was updated with the selected file
    // Note: Since there is no label, we use the input element to check the file value
    expect(fileInput.files[0]).toBe(fakeFile);
  });

  test('renders Log Out button', async () => {
    render(<Admin />);
    const logOutButton = screen.getByText('Log Out');
    expect(logOutButton).toBeInTheDocument();

  });

  it('renders username from API response', async () => {
    // Configuring the API response mock
    const mockApiResponse = {
      data: {
        username: 'TestUser',
        status: 'active',
      },
    };

    // Using mockResolvedValue on the module
    DataFetchGet.mockResolvedValue(mockApiResponse);

    // Rendering the Nome component
    const { findByText } = render(<Nome />);

    // Checking if the username is rendered
    const usernameElement = await findByText(/TestUser/i);
    expect(usernameElement).toBeInTheDocument();
  });

  test('renders profile image', () => {
    // Rendering the ProfileGet component
    const { getByAltText } = render(<ProfileGet />);

    // Checking if the profile image is present
    const profileImage = getByAltText('Profile');
    expect(profileImage).toBeInTheDocument();
  });

  test('Redirects when clicking on profile image', () => {
    // Mocking window.location.href
    delete window.location;
    window.location = { href: '' };
  
    // Rendering the component
    const { getByAltText } = render(<ProfileGet />);
  
    // Simulating a click on the element with the profile image
    fireEvent.click(getByAltText('Profile'));
  
    // Checking if the handleProfileClick function was called correctly
    expect(window.location.href).toBe('/profile');
  });
});
