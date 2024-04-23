// Se DataFetchPost estiver em outro modulo, importe-a aqui.
const DataFetchPost = require('../src/DataFetchFunctions/DataFetchPost.js');

// Crie um mock para a funcaoo
jest.mock('../src/DataFetchFunctions/DataFetchPost.js', () => {
    return jest.fn();
});

const { button_save } = require('../src/JAVASCRIPT/Create_Quiz/CreateQuizz.js');

describe('button_save function', () => {
    it('should call DataFetchPost with correct parameters', async () => {
        // Mock da resposta da DataFetchPost
        DataFetchPost.mockResolvedValue('mocked response');

        // Mock do console.log para verificar se ele e chamado corretamente
        global.console.log = jest.fn();

        const body = 'sampleBody';
        const options = 'sampleOptions';
        const opt_text = 'sampleText';
        const tag = 'sampleTag';
        const question_id = 'sampleQuestionID';

        await button_save(body, options, opt_text, tag, question_id);

        // Verifica se DataFetchPost foi chamado com os argumentos corretos
        expect(DataFetchPost).toHaveBeenCalledWith('api/REQ3/save-quiz', {
            question_id: question_id,
            body: body,
            options: options,
            explanation: 'explanation',
            opt_text: opt_text,
            tag: tag
        });

        // Verifica se console.log foi chamado com a resposta mockada
        expect(global.console.log).toHaveBeenCalledWith('mocked response');
    });
});
