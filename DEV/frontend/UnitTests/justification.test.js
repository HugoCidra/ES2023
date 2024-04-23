// justification.test.js

const { justification } = require('../src/JAVASCRIPT/Create_Quiz/CreateQuizz.js');

describe('justification', () => {
  test('should return false for an empty justification', () => {
    const input = '';
    const result = justification(input);
    expect(result).toBe(false);
  });

  test('should return true for a non-empty justification', () => {
    const input = 'This is a justification.';
    const result = justification(input);
    expect(result).toBe(true);
  });
});
