import React from 'react';
import ReactDOM from 'react-dom/client';
import './JAVASCRIPT/index.css';
import App from './JAVASCRIPT/App';
import reportWebVitals from './JAVASCRIPT/reportWebVitals';

/*
  Inicio do código
  O componente <App/> tem todos os outros componentes que formam o frontend dentro de si
*/

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
