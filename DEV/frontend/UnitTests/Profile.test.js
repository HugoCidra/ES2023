import React from 'react';
import { render, waitFor, screen } from '@testing-library/react';
import Profile  from '../src/JAVASCRIPT/Profile/Profile'; // Adjust import path as needed
import CreatorChart from '../src/JAVASCRIPT/Profile/Profile';
import SolverChartAnswers from '../src/JAVASCRIPT/Profile/Profile';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';
import { act } from 'react-dom/test-utils';
import '@testing-library/jest-dom';

jest.mock('../src/DataFetchFunctions/DataFetchGet');
beforeAll(() => {
  global.ResizeObserver = class ResizeObserver {
      constructor(cb) {
          this.cb = cb;
      }
      disconnect() {}
      observe(element, options) {}
      unobserve(element) {}
  };
});
jest.setTimeout(10000); 

// CreatorChart Tests
describe('CreatorChart', () => {

  

  it('renders no quizzes message when data is empty', async () => {
    DataFetchGet.mockResolvedValueOnce({ data: { data: [] } });
    render(<CreatorChart />);
    await waitFor(() => {
      expect(screen.getByText('You do not have approved or not approved quizzes!')).toBeInTheDocument();
    });
  });

  it('renders creator bar chart when data is available', async () => {
    // Mock the API calls
    DataFetchGet.mockImplementation(url => {
      if (url.endsWith('get_stats_solver/')) {
        return Promise.resolve({ data: { status: 401 } });
      } else if (url.endsWith('get_tags_creator/')) {
        return Promise.resolve({ data: { data: [{ x: 10, y: 5, name: 'TAG-1' }] } });
      }
    });
    
  
    render(<CreatorChart />);
  
    await waitFor(() => {
      // Log the mock calls to the console
    console.log(DataFetchGet.mock.calls);
      expect(screen.getByText('Quizzes')).toBeInTheDocument();
    });
  
    
  });

});


  // SolverChartAnswers Tests
describe('SolverChartAnswers', () => {
  it('renders a message when no tests have been solved', async () => {
    DataFetchGet.mockImplementation(url => {
      if (url.endsWith('get_stats_solver/')) {
        return Promise.resolve({
          data: {
            status: 200, // user is a solver
            data: []     // empty data, no tests solved
          }
        });
      }
    });
  
    render(<SolverChartAnswers />);
    await waitFor(() => {
      expect(screen.getByText('You have not solved any test yet!')).toBeInTheDocument();
    });
  });


  
  it('renders solver bar chart when data is available', async () => {
    
    DataFetchGet.mockImplementation(url => {
      if (url.endsWith('get_stats_solver/')) {
        return Promise.resolve({ data: { data: [{ x: 7, y: 3, name: 'Test1' }, { x: 5, y: 2, name: 'Test2' }] } });
      }
    });

    render(<SolverChartAnswers />);

    await waitFor(() => {
      
      expect(screen.getByText('Answers')).toBeInTheDocument();
    });
  });

  
});




// Profile Component Tests
describe('Profile', () => {
  it('renders CreatorChart for non-solver user', async () => {
    DataFetchGet.mockImplementation(url => {
      if (url.endsWith('get_stats_solver/')) {
        return Promise.resolve({ data: { status: 401 } });
      } else if (url.endsWith('get_tags_creator/')) {
        return Promise.resolve({ data: { data: [{ x: 10, y: 5, name: 'TAG-1' }] } });
      }
    });
    render(<Profile />);
    await waitFor(() => {
      expect(screen.getByText('Quizzes')).toBeInTheDocument();
    });
  });

  it('renders both CreatorChart and SolverChartAnswers for solver user', async () => {
    DataFetchGet.mockImplementation(url => {
      if (url.endsWith('get_stats_solver/')) {
        // Simulate a solver 
        return Promise.resolve({
          data: {
            status: 200,
            data: [{ x: 7, y: 3, name: 'Test1' }, { x: 5, y: 2, name: 'Test2' }]
          }
        });
      } else if (url.endsWith('get_tags_creator/')) {
        // data for the creatorChart
        return Promise.resolve({ data: { data: [{ x: 10, y: 5, name: 'TAG-2' }] } });
      }
    });
    render(<Profile />);
    await waitFor(() => {
      expect(screen.getByText('Quizzes')).toBeInTheDocument();
      expect(screen.getByText('Answers')).toBeInTheDocument();
    });
  });

  it('renders CreatorChart and a warning message for no tests solved', async () => {
    DataFetchGet.mockImplementation(url => {
      if (url.endsWith('get_stats_solver/')) {
        // Simulate a solver 
        return Promise.resolve({
          data: {
            status: 200,
            data: []
          }
        });
      } else if (url.endsWith('get_tags_creator/')) {
        // data for the creatorChart
        return Promise.resolve({ data: { data: [{ x: 10, y: 5, name: 'TAG-2' }] } });
      }
    });
    render(<Profile />);
    await waitFor(() => {
      expect(screen.getByText('Quizzes')).toBeInTheDocument();
      expect(screen.getByText('You have not solved any test yet!')).toBeInTheDocument();
    });
  });

  
});
  




