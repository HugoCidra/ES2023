// sixOptions.test.js

const { sixOptions } = require('../src/JAVASCRIPT/Create_Quiz/CreateQuizz.js');

test('sixOptions should return true for a valid set of six options', () => {
  const inputOptions = [
    { body: 'Option 1' },
    { body: 'Option 2' },
    { body: 'Option 3' },
    { body: 'Option 4' },
    { body: 'Option 5' },
    { body: 'Option 6' },
  ];

  const result = sixOptions(inputOptions);
  expect(result).toBe(true);
});

test('sixOptions should throw an error if there are fewer than six options', () => {
  const inputOptions = [
    { body: 'Option 1' },
    { body: 'Option 2' },
    { body: 'Option 3' },
    { body: 'Option 4' },
    { body: 'Option 5' }
  ];

  expect(() => sixOptions(inputOptions)).toThrowError("ERROR: You have to submit six options");
});
