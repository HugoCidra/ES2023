import React from 'react';
import { render } from '@testing-library/react';
import MenuModal from '../src/JAVASCRIPT/Menu/MenuModal'; 
import '@testing-library/jest-dom';


describe('MenuModal Component', () => {
  test('MenuModal component renders without crashing', () => {
    render(<MenuModal />);
  });

  test('Contêiner do modal possui a classe CSS correta', () => {
    const { container } = render(<MenuModal modal={true} />);
    expect(container.firstChild).toHaveClass('modal');
  });

  test('MenuModal corresponde ao snapshot anterior', () => {
    const { asFragment } = render(<MenuModal />);
    expect(asFragment()).toMatchSnapshot();
  });

});