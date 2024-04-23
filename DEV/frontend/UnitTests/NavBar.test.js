import React from 'react';
import { render, screen,fireEvent,waitFor } from '@testing-library/react';
import NavBar from '../src/JAVASCRIPT/NavBar/NavBar';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';

jest.mock('../src/DataFetchFunctions/DataFetchGet');


describe('TestList Component Tests', () => {
    const originalWindowLocation = window.location;
    beforeAll(() => {
      delete window.location;
      window.location = { originalWindowLocation, href: "/" };
    });
    
    afterAll(() => {
      window.location = originalWindowLocation;
    });

    test('1. renders NavBar component without errors', () => {
      render(<NavBar />);
    });

    

    test('3. displays the "Create Quiz" button in the navbar', async () => {
      render(<NavBar />);
      const createQuizButton = screen.getByText('Create Quiz');
      expect(createQuizButton)
    });
    
    test('4. displays the "Review Quiz" button in the navbar', async () => {
      render(<NavBar />);
      const reviewQuizButton = screen.getByText('Review Quiz');
      expect(reviewQuizButton)
    });
    
    test('5. displays the "Create Test" button in the navbar', async () => {
      render(<NavBar />);
      const createTestButton = screen.getByText('Create Test');
      expect(createTestButton)
    });
    
    test('6. displays the "Solve Test" button in the navbar', async () => {
      render(<NavBar />);
      const solveTestButton = screen.getByText('Solve Test');
      expect(solveTestButton)
    });
    
    test('7. solve_button_action redirects to / if the user does not have permissions', async () => {
      const mockData = { 
        data: {
            username:"JohnDoe",
            status: false
        }
      };
      DataFetchGet.mockResolvedValue(mockData);
      render(<NavBar />);
      const solveTestButton = screen.getByText('Solve Test');
      fireEvent.click(solveTestButton);
      expect(window.location.href).toBe('/');
    });
    
    test('8. solve_button_action redirects to /choose-test if the user is a solver', async () => {
      const mockData = { 
        data: {
            username: "JohnDoe",
            status: true
        }
      };
      DataFetchGet.mockResolvedValue(mockData);
  
      render(<NavBar />);
      const solveTestButton = screen.getByText('Solve Test');
      fireEvent.click(solveTestButton);
      expect(window.location.href).toBe('/choose-test');
    });
});
