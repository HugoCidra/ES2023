import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import MyQuizzes from '../src/JAVASCRIPT/Home_Page/Home';
jest.mock('../src/DataFetchFunctions/DataFetchGet');

describe('MyQuizzes', () => {

  test('1. Renders without errors', async () => {
    const mockData = {
      data: {
        unfinished_reproved_quizzes: [],
        creators: [],
        solvers: [],
      },
    };

      require('../src/DataFetchFunctions/DataFetchGet').default.mockResolvedValue(mockData);
      render(<MyQuizzes />);

      await waitFor(() => {
        expect(screen.getByText('My Quizzes'));
      });
    });

    test('2. Shows One Quizz', async () => {
      const mockData = {
        data: {
          unfinished_reproved_quizzes: [
            ['Quiz 1',1, 1],
          ],
          creators: [],
          solvers: [],
        },
      };
      require('../src/DataFetchFunctions/DataFetchGet').default.mockResolvedValue(mockData);
  
      render(<MyQuizzes />);
  
      await waitFor(() => {
        expect(screen.getByText('My Quizzes'));
        expect(screen.queryByText(/State: draft\nPergunta: Quiz 1/));
      });
    });

  test('3. Shows Multiple Quizzes with different States', async () => {
    const mockData = {
      data: {
        unfinished_reproved_quizzes: [
          ['Quiz 1',1, 1],
          ['Quiz 2',2, 2],
        ],
        creators: [],
        solvers: [],
      },
    };
    require('../src/DataFetchFunctions/DataFetchGet').default.mockResolvedValue(mockData);

    render(<MyQuizzes />);

    await waitFor(() => {
      expect(screen.getByText('My Quizzes'));
      expect(screen.queryByText(/State: draft\nPergunta: Quiz 1/));
      expect(screen.queryByText(/State: in evaluation\nPergunta: Quiz 2/));
    });
  });
  
});
