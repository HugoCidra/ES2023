
import React from 'react';
import QuizCard from './QuizCard';
import './CardsColumn.css';
import '../index.css'



function CardsColumn({ quizzes }) {
  return (
    <>
      <div className="MyQuizzes_column">
        {quizzes.map(item => (
          <div className="MyQuizzes_quizz_field" key={item[0]}>
            <QuizCard question={item[2]} state={item[1]} id={item[0]} />
          </div>
        ))}
      </div>
    </>
  );
}

export default CardsColumn;