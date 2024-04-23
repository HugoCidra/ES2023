import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import LoginForm from '../src/JAVASCRIPT/Login/Login';  


jest.mock('../src/DataFetchFunctions/DataFetchPut', () => ({
  __esModule: true,
  default: jest.fn()
}));

import DataFetchPut from '../src/DataFetchFunctions/DataFetchPut';

describe('Login', () =>{
  describe('logValue Tests', () =>{
    const originalWindowLocation = window.location;

    beforeAll(() => {
      delete window.location;
      window.location = { ...originalWindowLocation, href: "" };
    });
    
    afterAll(() => {
      window.location = originalWindowLocation;
    });

    test('1. Redirects to home on successful login', async () => {
      DataFetchPut.mockResolvedValueOnce({
        data: {
          status: 200,
          token: "sampleToken",
        },
      });

      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));

      await waitFor(() => {
        expect(window.location.href).toBe('/');
      });
    });

    test('2. Shows "Invalid Credentials" on unsuccessful login', async () => {
        DataFetchPut.mockResolvedValueOnce({ data: { status: 401 } });
        render(<LoginForm />);
        fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
        fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
        fireEvent.click(screen.getByText('Login'));
        await waitFor(() => expect(screen.getByText('Invalid Credentials!')));
    });

    test('3. Shows "Database Unreachable" when database cannot be reached', async () => {
        DataFetchPut.mockRejectedValueOnce(new Error());
        render(<LoginForm />);
        fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
        fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
        fireEvent.click(screen.getByText('Login'));
        await waitFor(() => expect(screen.getByText('Database Unreachable!')));
    });


    test('4. Handles promise rejection during database request', async () => {
        DataFetchPut.mockRejectedValueOnce(new Error());
        render(<LoginForm />);
        fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
        fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
        fireEvent.click(screen.getByText('Login'));
        await waitFor(() => expect(screen.getByText('Database Unreachable!')));
    });

    test('5. Handles invalid or unexpected input', async () => {
      DataFetchPut.mockResolvedValueOnce({ data: { unexpectedStructure: true } });
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: '' } });  // Invalid input
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));
      await waitFor(() => expect(screen.getByText('Invalid Credentials!')));
    });

    test('6. Displays the initial message correctly', () => {
      render(<LoginForm />);
      expect(screen.getByText(/If you already have an account please fill these fields to login./i));
    });

    test('7. Console logs correct data on unsuccessful login', async () => {
      const consoleSpy = jest.spyOn(console, 'log');
      DataFetchPut.mockResolvedValueOnce({ data: { status: 401, someData: 'errorData' } });
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));
      await waitFor(() => expect(consoleSpy).toHaveBeenCalledWith({status: 401, someData: 'errorData'}));
    });

    test('8. Stores token correctly on successful login', async () => {
      const fakeToken = 'valid-token';
      
      Storage.prototype.setItem = jest.fn();

      DataFetchPut.mockResolvedValueOnce({ data: { status: 200, token: fakeToken } });
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));

      await waitFor(() => expect(localStorage.setItem).toHaveBeenCalledWith('token', fakeToken));
      
      jest.resetAllMocks();
    });

    test('9. Sets log color correctly on error message', async () => {
      DataFetchPut.mockRejectedValueOnce(new Error());
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));
      await waitFor(() => expect(screen.getByText('Database Unreachable!')).toHaveStyle('color: red'));
    });

    test('10. Handles unexpected API response structure', async () => {
      DataFetchPut.mockResolvedValueOnce({ data: { unexpectedStructure: true } });
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));
      await waitFor(() => expect(screen.getByText('Invalid Credentials!')));
    });

    test('11. Handles missing token on successful status code', async () => {
      DataFetchPut.mockResolvedValueOnce({ data: { status: 400 } });
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));
      await waitFor(() => expect(screen.getByText('Invalid Credentials!')));
    });


    test('12. Renders input fields and login button', () => {
      render(<LoginForm />);
      expect(screen.getByTestId('username-input'));
      expect(screen.getByTestId('password-input'));
      expect(screen.getByText('Login'));
    });

    test('13. Test DataFetchPut with null token', async () => {
      localStorage.setItem("token", null);
      DataFetchPut.mockResolvedValueOnce({ data: { status: 401 } });
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));
      await waitFor(() => expect(screen.getByText('Invalid Credentials!')));
    });

    test('14. Test DataFetchPut with invalid token', async () => {
      localStorage.setItem("token", 'invalidToken');
      DataFetchPut.mockResolvedValueOnce({ data: { status: 401 } });
      render(<LoginForm />);
      fireEvent.change(screen.getByTestId('username-input'), { target: { value: 'user' } });
      fireEvent.change(screen.getByTestId('password-input'), { target: { value: 'pass' } });
      fireEvent.click(screen.getByText('Login'));
      await waitFor(() => expect(screen.getByText('Invalid Credentials!')));
    });
  });
});

