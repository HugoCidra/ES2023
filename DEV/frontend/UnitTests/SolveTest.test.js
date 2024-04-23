import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import DataFetchPost from '../src/DataFetchFunctions/DataFetchPost';
import SolveTest from '../src/JAVASCRIPT/Solve_Test/SolveTest';

/**
 * Mock the DataFetchGet function
 */
//Mock DataFetchPosr to avoid real calls

afterEach(() => {
  //Clear data after each test
  jest.clearAllMocks();
});

jest.mock('../src/DataFetchFunctions/DataFetchPost', () => ({
  __esModule: true,
  default: jest.fn(),
}));

jest.mock('../src/DataFetchFunctions/DataFetchGet', () => ({
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
      results: [],
    },
  }),
}));


it('should fetch test data on component mount', async () => {
  render(<SolveTest />);

  expect(require('../src/DataFetchFunctions/DataFetchGet').default).toHaveBe

  await waitFor(() => {

    expect(screen.getAllByText('ola')).toHaveLength(1);
  });
});


/**
 * Test whether the handleCancel function of the SolveTest component confirms the action and redirects
 */
test('handleCancel function should confirm and redirect', () => {
  // Set the initial URL to YourDomain/1
  const initialHref = 'SolveTest/1';
  Object.defineProperty(window, 'location', {
    value: { href: initialHref },
    writable: true,
  });

  window.confirm = jest.fn(() => true);

  const { container } = render(<SolveTest />);
  const cancelBtn = container.querySelector('CANCEL');

  fireEvent.click(cancelBtn);

  expect(window.confirm).toHaveBeenCalledWith("Are you sure you want to go to homepage?");
  expect(window.location.href).toBe('..');
});

test('handleCancel does not redirect when canceled', async () => {
  // Set the initial URL to YourDomain/1
  const initialHref = 'SolveTest/1';
  Object.defineProperty(window, 'location', {
    value: { href: initialHref },
    writable: true,
  });

  window.confirm = jest.fn(() => false);

  const { container } = render(<SolveTest />);
  const cancelBtn = container.querySelector('CANCEL');

  fireEvent.click(cancelBtn);

  expect(window.confirm).toHaveBeenCalledWith("Are you sure you want to go to homepage?");
  expect(window.location.href).toBe('..');
});

window.alert = jest.fn();
describe('handleSubmit', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('handle successful API response', async () => {
    const mockEvent = {preventDefault: jest.fn(),}

    //Mock the successful response data
    const successfulResponse = { data: {status: 500, log: ""}}

    // Create an instance of your component or class
    const yourComponentInstance = new SolveTest(successfulResponse);

    // Call the handleSubmit function
    await yourComponentInstance.handleSubmit(mockEvent);

    // Assertions
    expect(DataFetchPost).toHaveBeenCalledWith('api/REQ5/grade_test/', expect.any(String));
    expect(window.alert).not.toHaveBeenCalled(); // Ensure alert is not called
  });

  test('handles already done test', async () => {
    // Similar setup as the first test, but mock the response for "already done test"

    const mockEvent = {
      preventDefault: jest.fn(),
    };

    const alreadyDoneResponse = { data: { status: 501, log: 'Already done test' } };
    DataFetchPost.mockResolvedValueOnce(alreadyDoneResponse);

    const yourComponentInstance = new SolveTest(alreadyDoneResponse);

    await yourComponentInstance.handleSubmit(mockEvent);

    // Assertions
    expect(window.alert).toHaveBeenCalledWith("You've already done this test!");
    expect(window.location.href).toBe('..');
  });
});
