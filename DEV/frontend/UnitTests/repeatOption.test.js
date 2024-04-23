// Import the function to be tested
const { repeatOption } = require('../src/JAVASCRIPT/Create_Quiz/CreateQuizz.js');

// Describe the test suite
describe('repeatOption', () => {
  it('should return true for repeated answer options', () => {
    const listoptions = [
      { body: 'Option A' },
      { body: 'Option B' },
      { body: 'Option A' }, // This is a repeated option
      { body: 'Option C' },
      { body: 'Option D' },
      { body: 'Option E' },
    ];
    const result = repeatOption(listoptions);
    expect(result).toBe(true);
  });

  it('should return false for unique answer options', () => {
    const options = [
      { body: 'Option A' },
      { body: 'Option B' },
      { body: 'Option C' },
      { body: 'Option D' },
      { body: 'Option E' },
      { body: 'Option F' },
    ];
    const result = repeatOption(options);
    expect(result).toBe(false);
  });

  it('should return false for empty options list', () => {
    const options = [];
    const result = repeatOption(options);
    expect(result).toBe(false);
  });
});
