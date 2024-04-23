import './MyQuizzes.css';
import '../index.css'
import './FilterQuizzes.css';
import React from 'react';


function FilterQuizzes({changeFilter}){
    const handleChangeFilter = (event) => {
        changeFilter(parseInt(event.target.value));
    }
    
    return (
        <form>
            <select className = "filter" onChange={handleChangeFilter} >
                <option value = "0">All</option>
                <option value = "1">Draft</option>
                <option value = "2">Pending</option>
                <option value = "3">Rejected</option>
                <option value = "4">Accepted</option>
            </select>
        </form>

      );
}

export default FilterQuizzes;