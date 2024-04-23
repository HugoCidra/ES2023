const { chooseCorrect } = require('../src/JAVASCRIPT/Create_Quiz/CreateQuizz.js'); // Update with the correct file path

test('chooseCorrect should return true for a valid set of options', () => {
    const options = [
      { is_correct: true },
      { is_correct: false },
      { is_correct: false },
      { is_correct: false },
      { is_correct: false },
      { is_correct: false },
    ];
  
    const result = chooseCorrect(options);
    expect(result).toBe(true);
  });
  
  test('chooseCorrect should return false if there are no options', () => {
    const options = [];
  
    const result = chooseCorrect(options);
    expect(result).toBe(false);
  });
  