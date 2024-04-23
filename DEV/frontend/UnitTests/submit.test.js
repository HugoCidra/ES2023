import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import RegisterForm from '../src/JAVASCRIPT/Login/Login';  

jest.mock('../src/DataFetchFunctions/DataFetchPost', () => ({
  __esModule: true,
  default: jest.fn()
}));

import DataFetchPost from '../src/DataFetchFunctions/DataFetchPost';

describe('Login', () =>{
    describe('submit Tests', () =>{
        const originalWindowLocation = window.location;

        beforeAll(() => {
          delete window.location;
          window.location = { ...originalWindowLocation, href: "" };
        });
        
        afterAll(() => {
          window.location = originalWindowLocation;
        });
        
test('1. Initial Form Rendering ', () => {
    render(<RegisterForm />);
    expect(screen.getByTestId('username-input'));
    expect(screen.getByTestId('password-input'));
    expect(screen.getByText('Register'));
  });

  test('2. Redirects to home on successful registration', async () => {
    DataFetchPost.mockResolvedValueOnce({
      data: {
        status: 200,
        token: "sampleToken",
      },
    });
  
    render(<RegisterForm />);
    fireEvent.change(screen.getByTestId('username-input2'), { target: { value: 'validUser' } });
    fireEvent.change(screen.getByTestId('password-input2'), { target: { value: 'validPass123' } });
    fireEvent.click(screen.getByText('Register'));
    await waitFor(() => {
      expect(window.location.href).toBe('/');
    });
  });
  
  test('3. Shows "Username already exists!" on 500 status code', async () => {
    DataFetchPost.mockResolvedValueOnce({ data: { status: 500 } });
    render(<RegisterForm />);
    fireEvent.change(screen.getByTestId('username-input2'), { target: { value: 'existingUser' } });
    fireEvent.change(screen.getByTestId('password-input2'), { target: { value: 'validPass123' } });
    await fireEvent.click(screen.getByText('Register'));
    await waitFor(() => {
      expect(screen.getByText("Username already exists!"));
    });
  });
  
  test('4. Shows "Username must be between 6 and 18 characters" when an invalid username is provided', async () => {
    render(<RegisterForm />);
    fireEvent.change(screen.getByTestId('username-input2'), { target: { value: 'abc' } });
    fireEvent.change(screen.getByTestId('password-input2'), { target: { value: 'validPass123' } });
    await fireEvent.click(screen.getByText('Register'));
    await waitFor(() => {
      expect(screen.getByText("Username must be between 6 and 18 characters"));
    });
  });
  
  test('5. Shows "Password must be between 8 and 18 characters" when an invalid password is provided', async () => {
    render(<RegisterForm />);
    fireEvent.change(screen.getByTestId('username-input2'), { target: { value: 'validUser' } });
    fireEvent.change(screen.getByTestId('password-input2'), { target: { value: 'pass' } });
    await fireEvent.click(screen.getByText('Register'));
    await waitFor(() => {
      expect(screen.getByText("Password must be between 8 and 18 characters"));
    });
  });
  
  test('6. Shows "Username must contain only alphanumerical characters, \'-\' and \'_\'" when an invalid username is provided', async () => {
    render(<RegisterForm />);
    fireEvent.change(screen.getByTestId('username-input2'), { target: { value: 'user*name' } });
    fireEvent.change(screen.getByTestId('password-input2'), { target: { value: 'validPass123' } });
    await fireEvent.click(screen.getByText('Register'));
    await waitFor(() => {
      expect(screen.getByText("Username must contain only alphanumerical characters, '-' and '_'"));
    });
  });
  
  test('7. Shows "Password must contain only alphanumerical characters, \'-\', \'_\', \'#\', \'$\', \'%\', \'&\' and \'@\'" when an invalid password is provided', async () => {
    render(<RegisterForm />);
    fireEvent.change(screen.getByTestId('username-input2'), { target: { value: 'validUser' } });
    fireEvent.change(screen.getByTestId('password-input2'), { target: { value: 'invalidPass*' } }); 
    fireEvent.click(screen.getByText('Register'));
  
    await waitFor(() => {
      expect(screen.getByText("Password must contain only alphanumerical characters, \'-\', \'_\', \'#\', \'$\', \'%\', \'&\' and \'@\'"))
    });
  });
  
});
});
