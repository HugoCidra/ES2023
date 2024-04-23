import React from 'react';
import { render, fireEvent,screen, waitFor, redirectTo } from '@testing-library/react';
import FileB from '../src/JAVASCRIPT/Admin/Admin';
import DataFetchGet from '../src/DataFetchFunctions/DataFetchGet';
import '@testing-library/jest-dom';

jest.mock('../src/DataFetchFunctions/DataFetchGet');
beforeAll(() => {
  global.ResizeObserver = class ResizeObserver {
      constructor(cb) {
          this.cb = cb;
      }
      disconnect() {}
      observe(element, options) {}
      unobserve(element) {}
  };
});


describe('FileB', () => {


    test('testB - deve renderizar sem erros', () => {
        render(<FileB />);
        // Se o componente for renderizado sem erros, o teste passará.
    });

    test('deve conter um botão de exportação', () => {
        render(<FileB />);
        const botao = screen.getByRole('button', { name: 'Export' });
        expect(botao).toBeInTheDocument();
    });

    test('deve renderizar conteúdo (não estar vazio)', () => {
        const { container } = render(<FileB />);
        expect(container.firstChild).toBeTruthy();
    });

});
