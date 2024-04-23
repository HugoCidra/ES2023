// characterInput.test.js

const { characterInput } = require('../src/JAVASCRIPT/Create_Quiz/CreateQuizz');

describe('characterInput', () => {
  // Test case 1: should return true for valid characters
  test('should return true for valid characters', () => {
    const input = 'ABC123?!';
    const result = characterInput(input);
    expect(result).toBe(true);
  });

  // Test case 2: should return true for an empty string
  test('should return true for an empty string', () => {
    const input = '';
    const result = characterInput(input);
    expect(result).toBe(true);
  });

  // Test case 3: should return false for invalid characters
  test('should return false for invalid characters', () => {
    const input = '@#$%^&';
    const result = characterInput(input);
    expect(result).toBe(false);
  });
  
  // Test case 4: should return true for a valid string with special characters
  test('should return true for a valid string with special characters', () => {
    const input = 'Hello, World!?';
    const result = characterInput(input);
    expect(result).toBe(true);
  });
});
