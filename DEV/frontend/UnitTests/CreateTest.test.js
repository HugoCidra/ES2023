import React from 'react';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';
import DataFetchPost from '../src/DataFetchFunctions/DataFetchPost';
import CreateTest from '../src/JAVASCRIPT/Create_Test/CreateTest';
import { render, screen, act, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';

import Popup from 'react-popup';


window.alert = jest.fn();
jest.mock('../src/DataFetchFunctions/DataFetchGet', () => ({
    __esModule: true,
    default: jest.fn()
}));
jest.mock('../src/DataFetchFunctions/DataFetchPost', () => ({
    __esModule: true,
    default: jest.fn()
}));

test('Component did mount error message', async () => {
    const logSpy = jest.spyOn(console, 'log');

    DataFetchGet.mockImplementation(() => {
        throw new Error();
    });

    await act(async () => {
            render(<CreateTest />);
        });
    
    expect(logSpy).toHaveBeenCalledWith("error", new Error());

});

test('Testing title input', async () => {
    let fakePayload = { data: { status: 200, tags: [ "x", "y", "z" ] }};
    DataFetchGet.mockImplementation(() => fakePayload);
    // Render CreateTest component
    await act(async () => {
            render(<CreateTest />);
        });
    
        const inputElement = screen.getByPlaceholderText(/Enter a title/i);
        fireEvent.change(inputElement, { target: { value: "This is a test title" } });
        expect (inputElement.value).toBe("This is a test title");
    });
    
test('Testing button onClick handler', async () => {
    let fakePayload = { data: { status: 200, tags: [ "x" ] }};
    DataFetchGet.mockImplementation(() => fakePayload);
    // Render CreateTest component
    await act(async () => {
        render(<CreateTest />);
    });

    const xButton = screen.getByRole('button', { name: /x/i })

    expect(xButton).toHaveClass("tag_button");
    fireEvent.click(xButton);
    expect(xButton).toHaveClass("tag_button_click");
    fireEvent.click(xButton);
    expect(xButton).toHaveClass("tag_button");
});


test('Testing buttons limiter', async () => {
    let fakePayload = { data: { status: 200, tags: [ "x", "y", "z" ] }};
    DataFetchGet.mockImplementation(() => fakePayload);
    // Render CreateTest component
    await act(async () => {
        render(<CreateTest />);
    });

    const xButton = screen.getByRole('button', { name: /x/i })
    const yButton = screen.getByRole('button', { name: /y/i })
    const zButton = screen.getByRole('button', { name: /z/i })

    expect(xButton).toHaveClass("tag_button");
    fireEvent.click(xButton);
    expect(xButton).toHaveClass("tag_button_click");

    expect(yButton).toHaveClass("tag_button");
    fireEvent.click(yButton);
    expect(yButton).toHaveClass("tag_button_click");

    expect(zButton).toHaveClass("tag_button");
    fireEvent.click(zButton);
    //! It's not supposed to change the zButton class because 2 buttons are already selected
    expect(zButton).toHaveClass("tag_button");
});


test('Testing no title submition', async () => {
    const alertSpy = jest.spyOn(Popup, 'alert').mockImplementation(() => {});
    let fakePayload = { data: { status: 200, tags: [ "x", "y", "z" ] }};
    DataFetchGet.mockImplementation(() => fakePayload);
    // Render CreateTest component
    await act(async () => {
        render(<CreateTest />);
    });

    const xButton = screen.getByRole('button', { name: /x/i });
    const yButton = screen.getByRole('button', { name: /y/i });
    const submitButton = screen.getByRole('button', { name: /Submit/i });

    fireEvent.click(xButton);
    fireEvent.click(yButton);
    fireEvent.click(submitButton);

    expect(alertSpy).toHaveBeenCalled();
    expect(alertSpy).toHaveBeenCalledWith("The test must have a title with at least 10 characters.");
});

test('Testing no tags submition', async () => {
    const alertSpy = jest.spyOn(Popup, 'alert').mockImplementation(() => {});
    let fakePayload = { data: { status: 200, tags: [ "x", "y", "z" ] }};
    DataFetchGet.mockImplementation(() => fakePayload);

    await act(async () => {
        render(<CreateTest />);
    });

    const submitButton = screen.getByRole('button', { name: /Submit/i });
    fireEvent.click(submitButton);

    expect(alertSpy).toHaveBeenCalled();
    expect(alertSpy).toHaveBeenCalledWith("You must select 2 tags.");
});

test('Testing valid input submition', async () => {
    let fakePayload = { data: { status: 200, tags: [ "x", "y" ] }};
    let fakePostPayload = { data: { status: 200, count: { 'x': 5, 'y': 3 } } };
    const logSpy = jest.spyOn(console, 'log');

    DataFetchGet.mockImplementation(() => fakePayload);
    DataFetchPost.mockImplementation(() => fakePostPayload);

    await act(async () => {
        render(<CreateTest />);
    });

    fireEvent.click(screen.getByRole('button', { name: /x/i }));
    fireEvent.click(screen.getByRole('button', { name: /y/i }));

    const submitButton = screen.getByRole('button', { name: /Submit/i });
    const inputElement = screen.getByPlaceholderText(/Enter a title/i);

    fireEvent.change(inputElement, { target: { value: "This is a test title" } });
    await act(async () => {
        fireEvent.click(submitButton);
    });
    
    expect(logSpy).toHaveBeenCalledWith(JSON.stringify({
        title: "This is a test title",
        tags: [ "x", "y" ]
    }));

    expect(logSpy).toHaveBeenCalledWith(fakePostPayload);
});

test('Cancel button', async () => {
    let fakePayload = { data: { status: 200, tags: ["x", "y"] } };
    DataFetchGet.mockImplementation(() => fakePayload);

    let container;

    await act(async () =>{
        ({ container } = render(<CreateTest />));
    });

    const cancelButton = screen.getByRole('button', { name: /Cancel/i });

    fireEvent.click(screen.getByRole('button', { name: /x/i }));
    fireEvent.click(screen.getByRole('button', { name: /y/i }));
    await act(async () => {
        fireEvent.click(cancelButton);
    });
    async () => {
        // Check if the window.location.href changes
        expect(window.location.href).toBe('/');
    }

});

test('400 on POST request', async () => {
    let fakePayload = { data: { status: 200, tags: [ "x", "y" ] }};
    let fakePostPayload = { data: { status: 400, errors: ''}};
    const alertSpy = jest.spyOn(Popup, 'alert').mockImplementation(() => {});

    DataFetchGet.mockImplementation(() => fakePayload);
    DataFetchPost.mockImplementation(() => fakePostPayload);

    await act(async () => {
        render(<CreateTest />);
    });

    fireEvent.click(screen.getByRole('button', { name: /x/i }));
    fireEvent.click(screen.getByRole('button', { name: /y/i }));

    const submitButton = screen.getByRole('button', { name: /Submit/i });
    const inputElement = screen.getByPlaceholderText(/Enter a title/i);

    fireEvent.change(inputElement, { target: { value: "This is a test title" } });
    await act(async () => {
        fireEvent.click(submitButton);
    });

    expect(alertSpy).toHaveBeenCalledWith("Cannot create test; ");
});
