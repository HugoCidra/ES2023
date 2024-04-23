// questao.test.js

const { questao } = require('../src/JAVASCRIPT/Create_Quiz/CreateQuizz.js');

describe('questao', () => {
  test('should return false for an empty question', () => {
    const input = '';
    const result = questao(input);
    expect(result).toBe(false);
  });

  test('should return true for a non-empty question', () => {
    const input = 'What is your question?';
    const result = questao(input);
    expect(result).toBe(true);
  });
});
