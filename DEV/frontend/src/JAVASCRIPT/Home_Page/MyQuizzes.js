// MyQuizzes.js
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import CardsColumn from './CardsColumn';
import FilterQuizzes from './FilterQuizzes';
import './MyQuizzes.css';
import '../index.css'
import React, { useState, useEffect } from 'react';
import SearchBar from "../SearchBar/SearchBar";

function MyQuizzes() {
    const [myQuizzes, setMyQuizzes] = useState([[[]]]);

    const [filter, setFilter] = useState();

    const [myFilteredQuizzes, setMyFilteredQuizzes] = useState([[[]]]);

    const [columnsCount, setColumnsCount] = useState(3); // Initial number of columns


    useEffect(() => {
    async function fetchData() {
      try {
        const response = await DataFetchGet('api/REQ2/unfinished_reproved/', null);
        if (response.data.unfinished_reproved_quizzes === undefined) {
          window.location.href = "/login";
        } else {
          const quizzes = response.data.unfinished_reproved_quizzes;
          console.log("Quizes:",quizzes);
          if (filter) {
            const filteredQuizzes =  quizzes.filter((quiz) => quiz[1] === filter);
            setMyQuizzes(filteredQuizzes);
            setMyFilteredQuizzes(filteredQuizzes);
          } else {
             setMyQuizzes(quizzes);
             setMyFilteredQuizzes(quizzes);
         }
         console.log(response);
         
        }
      } catch (error) {
        console.error(error);
      }
    }

    fetchData();
  }, [filter]); 

  const changeFilter = (filter) => {
    setFilter(filter);
  }


    const handleSearch = (searchTerm) => {
        console.log('MyQuizzes pesquisando por:', searchTerm);
        
        const filteredQuizzes = myQuizzes.filter(quiz => quiz[2] && quiz[2].toLowerCase().includes(searchTerm.toLowerCase()));
        setMyFilteredQuizzes(filteredQuizzes)

        console.log(filteredQuizzes);
    };

    
  

   // Divide quizzes into the specified number of columns
  const columns = Array.from({ length: columnsCount }, (_, index) =>
  myFilteredQuizzes.filter((_, i) => i % columnsCount === index)
  );

  // Function to update the number of columns based on screen width
  const updateColumnsCount = () => {
    const screenWidth = window.innerWidth;
    /*if (screenWidth >= 1240) {*/ 
    if (screenWidth >= 1300) {
      setColumnsCount(3);
    } else if (screenWidth >= 925) {
      setColumnsCount(2);
    } else {
      setColumnsCount(1);
    }
  };

  // Attach the updateColumnsCount function to the window resize event
  useEffect(() => {
    updateColumnsCount();
    window.addEventListener('resize', updateColumnsCount);

    // Cleanup the event listener on component unmount
    return () => {
      window.removeEventListener('resize', updateColumnsCount);
    };
  }, []);

  // Render the CardsColumn components dynamically based on the number of columns
  const columnsComponents = columns.map((column, index) => (
    <CardsColumn key={index} quizzes={column} columnIndex={index + 1} />
  ));


  return (
    <div className='my-quizzes-body'>
      <div className='my-quizzes-header'>
      <h1 className="MyQuizzes_title">My Quizzes</h1>
      <div className='my-quizzes-search-bar'>
        <SearchBar onSearch={handleSearch}/>
        <FilterQuizzes changeFilter={changeFilter} />
      </div>
      </div>
      <div className='MyQuizzes_field hidden-scrollbar'>{columnsComponents}</div>
    </div>
  );
}

export default MyQuizzes;