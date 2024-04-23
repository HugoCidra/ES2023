import React, { useState, useEffect } from 'react';
import MyQuizzes from './MyQuizzes'; // Import MyQuizzes component
import HallOfFame from './HallOfFame'; // Import HallOfFame component
import NavBar from '.././NavBar/NavBar';
import Arrow from './Arrow.js';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import './Home.css';
import '../index.css';
import Popup from 'react-popup';

function Home() {
  async function solveButtonAction() {
    try {
      const payload = await DataFetchGet('api/REQ2/is_solver/', null);
      console.log(payload);
      if (payload.data.response === false) {
        Popup.alert("Must be a Solver");
        setTimeout(() => {
          Popup.close();
        }, 7000);
      } else {
        window.location.href = "/choose-test";
      }
    } catch (error) {
      console.error(error);
    }
  }

  // function solveButton() {
  //   return (
  //     <>
  //       <button className="button button_home2" id="Solve_button" value="SOLVE TEST" onClick={solveButtonAction}>
  //         SOLVE TEST
  //       </button>
  //     </>
  //   );
  // }

  return (
    <>
      <main>
        <NavBar />
        <div className='home-body'>
        <div id='my-quizzes'><MyQuizzes /></div> 
        <div id='HOF'><HallOfFame /></div>
        </div>
        <Arrow />
      </main>
    </>
  );
}

export default Home;






