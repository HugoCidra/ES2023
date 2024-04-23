import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import TestList from '../src/JAVASCRIPT/Choose_Test/ChooseTest';

jest.mock('../src/DataFetchFunctions/DataFetchGet', () => ({
    __esModule: true,
    default: jest.fn()
  }));

import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';

describe('TestList Component test_chosen_action function', () => {
  const originalWindowLocation = window.location;

beforeAll(() => {
  delete window.location;
  window.location = { ...originalWindowLocation, href: "" };
});

afterAll(() => {
  window.location = originalWindowLocation;
});

  test('1. Redirects correctly for test_id "1"', async () => {
      const mockData = { 
          data: {
              tests: [
                  {
                      title: "Test 1",
                      id: "1",
                      tags: ["tag1", "tag2"]
                  }
              ]
          }
      };
      DataFetchGet.mockResolvedValue(mockData);
  
      render(<TestList />);
  
      const testAElement = await screen.findByText('Test 1');
      fireEvent.click(testAElement);
      
      expect(window.location.href).toBe('/solve-test/1');
  });

  test('2. Redirects correctly for test_id "2"', async () => {
      const mockData = { 
          data: {
              tests: [
                  {
                      title: "Test 2",
                      id: "2",
                      tags: ["tag3", "tag4"]
                  }
              ]
          }
      };
      DataFetchGet.mockResolvedValue(mockData);
  
      render(<TestList />);
  
      const testElement = await screen.findByText('Test 2');
      fireEvent.click(testElement);
  
      expect(window.location.href).toBe('/solve-test/2');
  });
  
  test('3. Redirects correctly for test_id "3"', async () => {
      const mockData = { 
          data: {
              tests: [
                  {
                      title: "Test 3",
                      id: "3",
                      tags: ["tag5", "tag6"]
                  }
              ]
          }
      };
      DataFetchGet.mockResolvedValue(mockData);
  
      render(<TestList />);
  
      const testElement = await screen.findByText('Test 3');
      fireEvent.click(testElement);
  
      expect(window.location.href).toBe('/solve-test/3');
  });

  test('4. Redirects correctly for test_id "4"', async () => {
    const mockData = { 
        data: {
            tests: [
                {
                    title: "Test 4",
                    id: "4",
                    tags: ["tag7", "tag8"]
                }
            ]
        }
    };
    DataFetchGet.mockResolvedValue(mockData);

    render(<TestList />);

    const testElement = await screen.findByText('Test 4');
    fireEvent.click(testElement);

    expect(window.location.href).toBe('/solve-test/4');
});

test('5. Redirects correctly for test_id "5"', async () => {
    const mockData = { 
        data: {
            tests: [
                {
                    title: "Test 5",
                    id: "5",
                    tags: ["tag9", "tag10"]
                }
            ]
        }
    };
    DataFetchGet.mockResolvedValue(mockData);

    render(<TestList />);

    const testElement = await screen.findByText('Test 5');
    fireEvent.click(testElement);

    expect(window.location.href).toBe('/solve-test/5');
});

test('6. Redirects correctly for test_id "6"', async () => {
    const mockData = { 
        data: {
            tests: [
                {
                    title: "Test 6",
                    id: "6",
                    tags: ["tag11", "tag12"]
                }
            ]
        }
    };
    DataFetchGet.mockResolvedValue(mockData);

    render(<TestList />);

    const testElement = await screen.findByText('Test 6');
    fireEvent.click(testElement);

    expect(window.location.href).toBe('/solve-test/6');
});

});
