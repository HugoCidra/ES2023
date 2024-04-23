import React, {Component} from 'react';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import Login from '../src/JAVASCRIPT/Login/Login';
jest.mock('../src/DataFetchFunctions/DataFetchGet');
jest.mock('../src/DataFetchFunctions/DataFetchPut');


describe('Login', () => {

    


    test('1. Renders login without errors', async () => { //verificar que o render do login é como esperado

        render(<Login type = "login" />)

        await waitFor(()=> {
            expect(screen.getByText('Login'));
            expect(screen.getByText('Username'));
            expect(screen.getByText('Password'));
            expect(screen.getByText('Sign Up'));
            expect(screen.getByText('Submit'));


        })

        
    })

    test('2. Renders register without errors ', async()=>{ //verificar que o render do register funciona sem erros
        render(<Login type = "register"/>)
        expect(screen.getByText('Register'));
        expect(screen.getByText('Email'));
        expect(screen.getByText('Username'));
        expect(screen.getByText('Password'));
        expect(screen.getByText('Sign In'));
        expect(screen.getByText('Submit'));


    })

   
  
})
