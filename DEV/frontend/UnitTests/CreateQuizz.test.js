import React from 'react';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';
import DataFetchPost from '../src/DataFetchFunctions/DataFetchPost';
import CreateQuizz from '../src/JAVASCRIPT/Create_Quiz/CreateQuizz';
import { render, screen, act, fireEvent, waitForElement } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useParams } from 'react-router-dom';

import Popup from 'react-popup';

jest.mock('../src/DataFetchFunctions/DataFetchGet', () => ({
    __esModule: true,
    default: jest.fn()
}));

jest.mock('../src/DataFetchFunctions/DataFetchPost', () => ({
    __esModule: true,
    default: jest.fn()
}));

jest.mock('react-router-dom', () => ({
    ...jest.requireActual('react-router-dom'),
    useParams: jest.fn(),
    useRouteMatch: () => ({ url: '/create-quizz/id' }),
}));

beforeEach(() => {
    DataFetchGet.mockClear();
    DataFetchPost.mockClear();
    useParams.mockReturnValue({ undefined });
});

test('Test question input', async () => {
    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    const inputElement = screen.getByPlaceholderText(/What's your question?/i);
    fireEvent.change(inputElement, { target: { value: "This is a test quest" } });
    expect (inputElement.value).toBe("This is a test quest");
});

test('Test optional input', async () => {
    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    const inputElement = screen.getByPlaceholderText(/Optional Text?/i);
    fireEvent.change(inputElement, { target: { value: "This is a test option text" } });
    expect (inputElement.value).toBe("This is a test option text");
});

test('Test option 1 input', async () => {

    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    const inputElement = screen.getByPlaceholderText(/Option 1/i);
    await act(async () => {
        fireEvent.change(inputElement, { target: { value: "This is a test option text" } });
    });
    expect (inputElement.value).toBe("This is a test option text");
});

test('Test option 1 justification input', async () => {
    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    const inputElement = screen.getAllByPlaceholderText(/Justification/i)[0];
    await act(async () => {
        fireEvent.change(inputElement, { target: { value: "This is a test justification text" } });
    });
    expect (inputElement.value).toBe("This is a test justification text");
});

test('Test combobox', async () => {
    DataFetchGet.mockResolvedValue({ data: { status: 200, tags: [ "x", "y"] }});

    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    // find element with the text 'Select tags'
    const selectElement = screen.getByText(/Select tags/i);

    fireEvent.keyDown(selectElement.firstChild, { key: 'ArrowDown' });

    fireEvent.keyDown(selectElement.firstChild, { key: 'Enter' });
    expect(screen.getByText(/x/i)).toBeVisible();
    expect(screen.getByText(/y/i)).toBeVisible();

    fireEvent.keyDown(screen.getByText(/x/i), { key: 'Escape', code: 'Escape', charCode: 27 });
    
    expect(screen.queryByText(/x/i)).not.toBeNull();
    expect(screen.queryByText(/y/i)).toBeNull();

    fireEvent.keyDown(selectElement.firstChild, { key: 'ArrowDown' });
    fireEvent.keyDown(screen.getByText(/x/i), { key: 'Delete', code: 'Delete', charCode: 46  });

    expect(screen.queryByText(/x/i)).toBeNull();
    expect(screen.queryByText(/y/i)).toBeNull();

});

test('Empty question', async () => {
    const alertSpy = jest.spyOn(Popup, 'alert').mockImplementation(() => {});    
    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    /*search for the submit button */
    const submitButton = screen.getByRole('button', { name: /Submit/i });
    /* click the button */
    await act(async () => {
        fireEvent.click(submitButton);
    });
    
    expect(alertSpy).toHaveBeenCalledWith("ERROR: You have to submit your question.");
});


test('Correct submition', async () => {
    DataFetchGet.mockResolvedValue({ data: { status: 200, tags: [ "x" ] }});
    DataFetchPost.mockResolvedValue({ data: { status: 200 }});

    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    /* dont exepct a element with Quiz Submitted! text in the document*/
    expect(screen.queryByText(/Quiz Submitted!/i)).toBeNull();
    
    /* find me the question input */
    const questionInput = screen.getByPlaceholderText(/What's your question?/i);
    /* type the question */
    fireEvent.change(questionInput, { target: { value: "This is a test question" } });
    /* type the options */
    fireEvent.change(screen.getByPlaceholderText(/Option 1/i), { target: { value: "This is a test option 1" } });
    fireEvent.change(screen.getByPlaceholderText(/Option 2/i), { target: { value: "This is a test option 2" } });
    fireEvent.change(screen.getByPlaceholderText(/Option 3/i), { target: { value: "This is a test option 3" } });
    fireEvent.change(screen.getByPlaceholderText(/Option 4/i), { target: { value: "This is a test option 4" } });
    fireEvent.change(screen.getByPlaceholderText(/Option 5/i), { target: { value: "This is a test option 5" } });
    fireEvent.change(screen.getByPlaceholderText(/Option 6/i), { target: { value: "This is a test option 6" } });

    /* find the first input type radio element and click it*/
    const radio1 = screen.getAllByRole('radio')[0];
    fireEvent.click(radio1);

    const selectElement = screen.getByText(/Select tags/i);

    fireEvent.keyDown(selectElement.firstChild, { key: 'ArrowDown' });
    fireEvent.keyDown(selectElement, { key: 'Enter', code: 'Enter', charCode: 13 });
    // fireEvent.keyDown(screen.getByText(/x/i), { key: 'Delete', code: 'Delete', charCode: 46 });


    /* find submit */
    const submitButton = screen.getByRole('button', { name: /Submit/i });
    /* click submit */
    await act(async () => {
        fireEvent.click(submitButton);
    });

    expect(DataFetchPost).toHaveBeenCalledWith("api/REQ3/submit-quiz", {
        body: "This is a test question", explanation: "", opt_text: "", options: [
            { body: "This is a test option 1", id: 1, is_correct: true, justification: "" },
            { body: "This is a test option 2", id: 2, is_correct: false, justification: "" },
            { body: "This is a test option 3", id: 3, is_correct: false, justification: "" },
            { body: "This is a test option 4", id: 4, is_correct: false, justification: "" },
            { body: "This is a test option 5", id: 5, is_correct: false, justification: "" },
            { body: "This is a test option 6", id: 6, is_correct: false, justification: "" }
        ],
        check: true,
        question_id: 0, tags: ["x"]
    });

    // expect <button class="mm-popup__close"></button> to be in the document
    // expect(screen.getByRole('dialog')).toBeInTheDocument();
});

test('Correct save', async () => {
    const alertSpy = jest.spyOn(Popup, 'create').mockImplementation(() => {});
    DataFetchGet.mockResolvedValue({ data: { status: 200, tags: [ "x" ] }});
    DataFetchPost.mockResolvedValue({ data: { status: 200 }});

    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    /* Find the save button */
    const saveButton = screen.getByRole('button', { name: /Save/i });
    /* click submit */
    await act(async () => {
        fireEvent.click(saveButton);
    });
});

test('Tests DataBase not connected', async () => {
    const alertSpy = jest.spyOn(Popup, 'alert').mockImplementation(() => {});
    useParams.mockReturnValue({ id: 1 });

    DataFetchGet.mockImplementation((url,data=null) => {
        // If the url equals to 'api/REQ6/tags/' return { data: { success: 'no' }}
        if (url === 'api/REQ6/tags/') {
            return new Promise((resolve,reject)=>{
                resolve({ data: { status: 200, tags: [ "x" ] }});
            })
        }
        // else if url has 'api/REQ3/get-quiz/'
        else if (url.includes('api/REQ3/get-quiz/')) {
            return new Promise((resolve,reject)=>{
                resolve({ success:"no", data:{ data: undefined } });
            })
        }
    })

    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });   

    expect(alertSpy).toHaveBeenCalledWith("ERROR: DataBase is not connected");
    async () => {
        expect(window.location.href).toBe('/');
    }
})

test('Tests when data status equals to 404', async () => {
    const alertSpy = jest.spyOn(Popup, 'alert').mockImplementation(() => {});
    useParams.mockReturnValue({ id: 1 });

    DataFetchGet.mockImplementation((url,data=null) => {
        // If the url equals to 'api/REQ6/tags/' return { data: { success: 'no' }}
        if (url === 'api/REQ6/tags/') {
            return new Promise((resolve,reject)=>{
                resolve({ data: { status: 200, tags: [ "x" ] }});
            })
        }
        // else if url has 'api/REQ3/get-quiz/'
        else if (url.includes('api/REQ3/get-quiz/')) {
            return new Promise((resolve,reject)=>{
                resolve({ success:"???", data: { data: { status: 404, message: "a test message" } }});
            })
        }
        else if (url === 'api/REQ8/get_username/' || url === 'api/REQ2/is_solver/') {
            return { data: {username: "john doe", status: 200} }
        }
    })

    await act(async () => {
        render(<CreateQuizz />);
    });   

    expect(alertSpy).toHaveBeenCalledWith("ERROR: a test message");
    async () => {
        expect(window.location.href).toBe('/');
    }
})

test('Tests when there is success in retrieving info about the quiz', async () => {
    useParams.mockReturnValue({ id: 1 });

    DataFetchGet.mockImplementation((url,data=null) => {
        // If the url equals to 'api/REQ6/tags/' return { data: { success: 'no' }}
        if (url === 'api/REQ6/tags/') {
            return new Promise((resolve,reject)=>{
                resolve({ data: { status: 200, tags: [ "x", "y" ] }});
            })
        }
        // else if url has 'api/REQ3/get-quiz/'
        else if (url.includes('api/REQ3/get-quiz/')) {
            return new Promise((resolve,reject)=>{
                resolve({ success:"yes", data: { data: { status: "???", options: [
                    {id: 1, body: '', is_correct: false, justification: ''},
                    {id: 2, body: '', is_correct: false, justification: ''},
                    {id: 3, body: '', is_correct: false, justification: ''},
                    {id: 4, body: '', is_correct: false, justification: ''},
                    {id: 5, body: '', is_correct: false, justification: ''},
                    {id: 6, body: '', is_correct: false, justification: ''},
                ], question: "uma question especifica", tags: ["y"], opt_text : "", rejected_justifications: []} } });
            })
        }
        else if (url === 'api/REQ8/get_username/' || url === 'api/REQ2/is_solver/') {
            return { data: { username: "john doe", status: 200 } }
        }
    });

    // Render CreateQuizz component
    await act(async () => {
        render(<CreateQuizz />);
    });

    const questionInput = screen.getByDisplayValue(/uma question especifica/i);
    expect(questionInput).toBeVisible();
    //check if y is on screen
    expect(screen.getByText(/y/i)).toBeVisible();
});
