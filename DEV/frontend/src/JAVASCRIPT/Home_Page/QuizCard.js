// MyQuizzes.js
import React, { useState, useEffect } from 'react';
import './QuizCard.css';
import '../index.css'

const stateLabels = {
  1: "Draft",
  2: "Pending",
  3: "Rejected",
  4: "Accepted",
};

function QuizCard({ question, state, id }) {
  const draftRef = `/create-quizz/${id}`;

  const label = stateLabels[state];

  return (
    <a href={draftRef} className="Quiz_card" target="_self" rel="noopener">
        <p className={`MyQuizzes_quiz state_${state}`}>
          {question}
        </p>
        <div className={`Quiz_state state_${state}`}>
            {label}
        </div>
      </a>
  );

  // if (state === 1) {
  //   return (
  //     <a href={draftRef} target="_self" rel="noopener">
  //       <p className='MyQuizzes_quiz state_1'>
  //         draft<br />
  //         {question}
  //       </p>
  //       <div>
  //         <p className="Quiz_state state_1">
  //           Draft
  //         </p>
  //       </div>
  //     </a>
  //   );
  // } else if (state === 2) {
  //   return (
  //     <a href={draftRef} target="_self" rel="noopener">
  //       <p className='MyQuizzes_quiz state_2'>
  //         in evaluation<br />
  //         {question}
  //       </p>
  //       <div>
  //         <p className="Quiz_state state_2">
  //           Pending
  //         </p>
  //       </div>
  //     </a>
      
  //   );
  // } else if (state === 3) {
  //   return (
  //     <a href={draftRef} target="_self" rel="noopener">
  //       <p className='MyQuizzes_quiz state_3'>
  //         rejected<br />
  //         {question}
  //       </p>
  //       <div>
  //         <p className="Quiz_state state_3">
  //           Rejected
  //         </p>
  //       </div>
  //     </a>
  //   );
  // } else if (state === 4) {
  //   return (
  //     <a href={draftRef} target="_self" rel="noopener">
  //       <p className='MyQuizzes_quiz state_4'>
  //         accepted<br />
  //         {question}
  //       </p>
  //         <div>
  //           <p className="Quiz_state state_4">
  //             Accepted
  //           </p>
  //         </div>
  //     </a>
  //   );
  // }
}

export default QuizCard;
