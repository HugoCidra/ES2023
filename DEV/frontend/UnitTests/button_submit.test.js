import { button_submit } from '../src/JAVASCRIPT/Create_Quiz/CreateQuizz';
import { DataFetchPost } from '../src/DataFetchFunctions/DataFetchPost';

jest.mock('../src/DataFetchFunctions/DataFetchPost');

describe('button_submit function', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it('submits the quiz data correctly', async () => {
    const body = 'Test Question';
    const options = ['Option 1', 'Option 2', 'Option 3'];
    const opt_text = 'Test Optional Text';
    const tag = 'Test Tag';
    const question_id = 1;

    DataFetchPost.mockResolvedValueOnce({ success: true });

    const result = await button_submit(body, options, opt_text, tag, question_id);

    expect(result).toBe(true);
    expect(DataFetchPost).toHaveBeenCalledWith("api/REQ3/submit-quiz", {
      question_id: question_id,
      body: body,
      options: options,
      explanation: "",
      opt_text: opt_text,
      tag: tag
    });
  });
});