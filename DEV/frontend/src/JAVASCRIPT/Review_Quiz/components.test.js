import { ContainerJustificationSubmit, ButtonsAccRej } from './components';

import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';

jest.mock('../../DataFetchFunctions/DataFetchPost', () => ({
    __esModule: true,
    default: jest.fn()
}));

test('handleSubmit', () => {
    // Mocking DataFetchPost because it is called inside the function
    let fakePayload = { data: { status: 200, options: [0, 1, 2, 3, 4, 5] } };
    DataFetchPost.mockImplementation(() => fakePayload);

    // Initialization of the spy functions
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});
    const errorSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
    const logSpy = jest.spyOn(console, 'log');

    // Initialization of the Objects to test
    const justSubmit = new ContainerJustificationSubmit({id: 999});
    const accRej = new ButtonsAccRej();

    // ==========================|| acceptance === 2 ||=============================== //

    justSubmit.handleSubmit({preventDefault: () => 999});
    
    // Confirm that alert is called with the right argument
    expect(alertSpy).toHaveBeenCalled();
    expect(alertSpy).toHaveBeenLastCalledWith('You must either accept or reject the question.');
    
    // ==========================|| acceptance === 0 ||=============================== //

    // Changes acceptance 2 => 0
    accRej.handleSubmitRej({target: {className: 'placeholder'}});

    justSubmit.handleSubmit({preventDefault: () => 999});
    // Verify that the alert was called again (now in the acceptance === 0 block)
    expect(alertSpy).toHaveBeenCalledTimes(2);
    expect(alertSpy).toHaveBeenLastCalledWith('Your justification must contain more than 40 and fewer than 512 characters.');

    // Changes the state.value so that the alert isn't called
    justSubmit.state.value = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
    justSubmit.handleSubmit({preventDefault: () => 999});
    // Verify that the number of alert calls hasn't increased
    expect(alertSpy).toHaveBeenCalledTimes(2);
    
    // Verifies that console.log is called as expected
    expect(logSpy).toHaveBeenCalledTimes(3);
    expect(logSpy).toHaveBeenCalledWith(justSubmit.state);

    // Calls handleSubmit in order to enter the catch block and verify console.error is being called
    DataFetchPost.mockImplementation(() => {throw {response: 'erro'}});
    justSubmit.handleSubmit({preventDefault: () => 999});
    expect(errorSpy).toHaveBeenCalled();
});
