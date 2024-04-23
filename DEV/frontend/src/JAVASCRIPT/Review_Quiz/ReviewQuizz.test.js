import { render } from '@testing-library/react';
import ReviewQuizz from "./ReviewQuizz";
import { act } from "react-dom/test-utils";

import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';

jest.mock('../../DataFetchFunctions/DataFetchGet', () => ({
    __esModule: true,
    default: jest.fn()
}));

test('Checks if componentWillMount\'s if block is functioning correctly', async () => {

    // Initializate spy functions
    const logSpy = jest.spyOn(console, 'log');
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
    const spyWillMount = jest.spyOn(ReviewQuizz.prototype, 'componentWillMount');

    // ----- If block ----- //
    // Make status to be 200
    let fakePayload = { data: { status: 200, options: [0, 1, 2, 3, 4, 5] } };
    DataFetchGet.mockImplementation(() => fakePayload);

    // Render ReviewQuizz component
    await act(async () => {
        render(<ReviewQuizz/>);
    });

    // Test if componentWillMount is called
    expect(spyWillMount).toHaveBeenCalled();

    // Tests if DataFetchGet is called correctly
    expect(DataFetchGet).toHaveBeenCalledWith('api/REQ4/quiz/', null);

    // Test if console.log is called when status === 200
    expect(logSpy).toHaveBeenCalled();
    expect(logSpy).toHaveBeenCalledWith(fakePayload);

    // ----- Else block ----- //

    // Make status not to be 200
    fakePayload = { data: { status: 999, options: [0, 1, 2, 3, 4, 5] } };
    DataFetchGet.mockImplementation(() => fakePayload);

    // Render ReviewQuizz component
    await act(async () => {
        render(<ReviewQuizz/>);
    });

    // Test if componentWillMount is called
    expect(spyWillMount).toHaveBeenCalled();

    // Tests if DataFetchGet is called correctly
    expect(DataFetchGet).toHaveBeenCalled();
    expect(DataFetchGet).toHaveBeenCalledWith('api/REQ4/quiz/', null);

    // Tests if alert is called correctly
    expect(alertSpy).toHaveBeenCalled();
    expect(alertSpy).toHaveBeenCalledWith("There are no questions for you to review at this time.");
});
