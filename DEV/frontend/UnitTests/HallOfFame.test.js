import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import HallOfFame from '../src/JAVASCRIPT/Home_Page/HallOfFame';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet'

jest.mock('../src/DataFetchFunctions/DataFetchGet');

describe('HallOfFame', () => {
  test('1. Renders without errors', async () => {
    DataFetchGet.mockResolvedValue({ data: {unfinished_reproved_quizzes: [], creators: [], solvers: [] } });

    render(<HallOfFame />);

    await waitFor(() => {
      expect(screen.getByText('Hall of Fame'));
      expect(screen.getByText('Solvers'));
      expect(screen.getByText('Creators'));
      expect(screen.getByPlaceholderText('Search...'));
    });
  });

  test('2. Shows Solvers', async () => {
    const mockData = {
      data: {
        unfinished_reproved_quizzes: [],
        creators: [],
        solvers: [['Solver1', 100], ['Solver2', 200]],
      },
    };

    DataFetchGet.mockResolvedValue(mockData);

    render(<HallOfFame />);
    await waitFor(() => {
      expect(screen.getByText('Solver1'));
      expect(screen.getByText('Solver2'));
      expect(screen.getByText('100'));
      expect(screen.getByText('200'));
    });
  });

  test('3. Shows Creators', async () => {
    const mockData = {
      data: {
        unfinished_reproved_quizzes: [],
        creators: [['Creator1', 300], ['Creator2', 400]],
        solvers: [],
      },
    };

    DataFetchGet.mockResolvedValue(mockData);

    render(<HallOfFame />);

    await waitFor(() => {
      expect(screen.getByText('Creator1'));
      expect(screen.getByText('Creator2'));
      expect(screen.getByText('300'));
      expect(screen.getByText('400'));
    });
  });
  test('4. Shows Solvers and Creators', async () => {
    const mockData = {
      data: {
        unfinished_reproved_quizzes: [],
        creators: [['Creator1', 300], ['Creator2', 400]],
        solvers: [['Solver1', 100], ['Solver2', 200]],
      },
    };

    DataFetchGet.mockResolvedValue(mockData);

    render(<HallOfFame />);

    await waitFor(() => {
      expect(screen.getByText('Creator1'));
      expect(screen.getByText('Creator2'));
      expect(screen.getByText('300'));
      expect(screen.getByText('400'));
      expect(screen.getByText('Solver1'));
      expect(screen.getByText('Solver2'));
      expect(screen.getByText('100'));
      expect(screen.getByText('200'));
    });
  });

});


