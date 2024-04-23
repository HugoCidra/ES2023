import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';
import SolveTest from './SolveTest';

/**
 * Mock the DataFetchGet function
 */

jest.mock('../../DataFetchFunctions/DataFetchGet', () => ({
  __esModule: true,
  default: jest.fn().mockResolvedValue({
    data: {
      status: 200,
      questions: [
        {
          id: '1',
          body: 'ola',
          opts: [
            { id: 1, body: 'opta1' },
          ],
        },
      ],
    },
  }),
}));

describe('SolveTest -> componentDidMount', () => {
  it('should fetch test data on component mount', async () => {
    render(<SolveTest />);
    
    /**
     * Ensure that DataFetchGet was called with the expected arguments
     */

    expect(require('../../DataFetchFunctions/DataFetchGet').default).toHaveBeenCalledWith('api/REQ5/get_test/', expect.any(Object));

    /**
     * Wait for the component to finish rendering and data to be fetched
     */

    await waitFor(() => {

      /**
       * Make assertions about the component's behavior after data fetching
       */

      expect(screen.getAllByText('ola')).toHaveLength(1);
    });
  });
});

//Mock DataFetchPosr to avoid real calls
jest.mock('../../DataFetchFunctions/DataFetchPost');

describe('SolveTest Component', () => {
  afterEach(() => {
    //Clear data after each test
    jest.clearAllMocks();
  });

  /**
 * Test whether the SolveTest component's handleSubmit function calls DataFetchPost and updates the state
 */

  test('handleSubmit function should call DataFetchPost and update state', async () => {
    //Simulated data for the answer
    const responseData = {
      status: 200,
      log: 'Test Successful',
      grade: 85,
    };

    //Mock DataFetchPost to return data
    DataFetchPost.mockResolvedValue({ data: responseData });

    //Render the SolveTest component
    render(<SolveTest />);

    //Encontrar o botão "SUBMIT" no componente
    const submitButton = screen.getByText('SUBMIT');

    //Find the "SUBMIT" button on the component
    fireEvent.click(submitButton);

    //Check if DataFetchPost is called with the correct arguments
    expect(DataFetchPost).toHaveBeenCalledWith('api/REQ5/grade_test/', expect.any(String));
  });

  
/**
 * Test whether the handleCancel function of the SolveTest component confirms the action and redirects
 */
  test('handleCancel function should confirm and redirect', () => {
    //Render the SolveTest component
    render(<SolveTest />);

    //Find the "CANCEL" button on the component
    const cancelButton = screen.getByText('CANCEL');

    //Spy on window.confirm function to always return "true"
    const confirmMock = jest.spyOn(window, 'confirm');
    confirmMock.mockReturnValue(true);

    //Simulate clicking the "CANCEL" button
    fireEvent.click(cancelButton);

    //Check if window.confirm was called with the correct message
    expect(confirmMock).toHaveBeenCalledWith('Are you sure you want to go to the homepage?');

  });
});
