import React, { useState, useEffect } from 'react';
import './SearchBar.css';
import '../index.css'

const SearchBar = ({ onSearch, onFocus, onBlur, value }) => {
    const [searchBarText, setSearchBarText] = useState(value);

    useEffect(() => {
        setSearchBarText(value);
    }, [value]);

    useEffect(() => {
        onSearch(searchBarText);
    }, [searchBarText]);

    const funcInputChange = (e) => {
        setSearchBarText(e.target.value);

    };

    return (
            <input
                type="text"
                placeholder="Search..."
                value={searchBarText}
                className="SearchBar_input"
                onChange={funcInputChange}
                onFocus={onFocus ? () => onFocus() : null} 
                onBlur={onBlur ? () => onBlur() : null} 
                
            />

  
    );
};

export default SearchBar;


