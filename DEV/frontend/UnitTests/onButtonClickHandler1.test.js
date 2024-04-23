import { render, screen, fireEvent } from '@testing-library/react';
import Botao from 'D:/Aulas/3 Ano/ES/projeto es/pl1/DEV/frontend/src/JAVASCRIPT/Create_Quiz/CreateQuizz.js';
import { DataFetchPost } from 'D:/Aulas/3 Ano/ES/projeto es/pl1/DEV/frontend/src/DataFetchFunctions/DataFetchPost.js';

jest.mock('D:/Aulas/3 Ano/ES/projeto es/pl1/DEV/frontend/src/DataFetchFunctions/DataFetchPost.js');

describe('Botao component', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it('calls the onButtonClickHandler1 when SAVE button is clicked', () => {
    const body = 'Test Question';
    const options = ['Option 1', 'Option 2', 'Option 3'];
    const opt_text = 'Test Optional Text';
    const tag = 'Test Tag';
    const question_id = 1;

    DataFetchPost.mockResolvedValueOnce({ success: true });

    render(<Botao body={body} options={options} opt_text={opt_text} tag={tag} question_id={question_id} />);

    const saveButton = screen.getByValue('SAVE');
    fireEvent.click(saveButton);

    expect(DataFetchPost).toHaveBeenCalledWith("api/REQ3/save-quiz", {
      question_id: question_id,
      body: body,
      options: options,
      explanation: "explanation",
      opt_text: opt_text,
      tag: tag
    });

    // Check for UI changes after save operation
    // If you expect some UI change, uncomment the below line.
    // expect(screen.getByText('Quiz Saved!')).toBeInTheDocument();
  });
});