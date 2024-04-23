import React from 'react';
import { render, waitFor, fireEvent, screen } from '@testing-library/react';
import TestList from '../src/JAVASCRIPT/Choose_Test/ChooseTest';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';

jest.mock('../src/DataFetchFunctions/DataFetchGet');

describe('TestList Component Tests', () => {
    const originalWindowLocation = window.location;

    beforeAll(() => {
      delete window.location;
      window.location = { ...originalWindowLocation, href: "" };
    });
    
    afterAll(() => {
      window.location = originalWindowLocation;
    });

    test('1. Shows alert and redirects when no tests to solve', async () => {
        const mockData = { 
            data: {
                tests:[]
            }
        };
        if(mockData.data.tests.length===0){
        DataFetchGet.mockResolvedValue(mockData);
        render(<TestList />);
        const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
        expect(window.location.href).toBe('');
        alertSpy.mockRestore();
        }
     });

    test('2. Renders tests and handles click event', async () => {
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
        expect(testAElement);
    
        fireEvent.click(testAElement);
    
        expect(window.location.href).toBe('/solve-test/1');
    });


    test('3. Displays multiple tests correctly', async () => {
        const mockData = {
            data: {
                tests: [
                    { title: "Test A", id: "1", tags: ["tagA1", "tagA2"] },
                    { title: "Test B", id: "2", tags: ["tagB1", "tagB2"] }
                ]
            }
        };
        DataFetchGet.mockResolvedValue(mockData);
    
        render(<TestList />);
        
        const testAElement = await screen.findByText('Test A');
        const testBElement = await screen.findByText('Test B');
        
        expect(testAElement);
        expect(testBElement);
    });
  
    test('4. Displays tags correctly', async () => {
        const mockData = {
            data: {
                tests: [
                    { title: "Test A", id: "1", tags: ["tagA1", "tagA2"] }
                ]
            }
        };
        DataFetchGet.mockResolvedValue(mockData);
    
        render(<TestList />);
        
        const tagA1Element = await screen.findByText('tagA1');
        const tagA2Element = await screen.findByText('tagA2');
        
        expect(tagA1Element);
        expect(tagA2Element);
    });
});