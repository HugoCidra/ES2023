import React, { useState, useEffect } from 'react';
import '../index.css';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import "./ChooseTest.css";
import NavBar from '.././NavBar/NavBar';
import Popup from 'react-popup';

function ChooseTest() {
  const [selectedTag, setTag] = useState();
  const [searchQuery, setSearchQuery] = useState('');

  const changeTag = (filter2) => {
    setTag(filter2);
  };

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  return (
    <>
      <main>
        <NavBar />
        <h1 className="chooseTest_title">Choose a test to Solve</h1>
        <div className='bar_search_filter'>
        <div className="search-bar">
          <input
            type="text"
            placeholder="Search tests..."
            value={searchQuery}
            onChange={handleSearch}
          />
        </div>

        <FilterTests changeTag={changeTag} />
        </div>
        <TestList selectedTag={selectedTag} searchQuery={searchQuery} />
      </main>
    </>
  );
}

function FilterTests({ changeTag }) {
  const handleChangeTag = (event) => {
    changeTag(parseInt(event.target.value));
  }

  return (
    <form className='menu-form'>
      <select className="filter" onChange={handleChangeTag}>
        <option value="0">All</option>
        <option value="1">AC</option>
        <option value="2">BD</option>
        <option value="3">COMP</option>
        <option value="4">IPRP</option>
        <option value="5">POO</option>
        <option value="6">PPP</option>
        <option value="7">RC</option>
        <option value="8">SI</option>
        <option value="9">SO</option>
        <option value="10">TC</option>
        <option value="11">TI</option>
        <option value="12">ES</option>
      </select>
    </form>
  );
}

const tagsLabels = {
  0:"All",
  1:"AC",
  2:"BD",
  3:"COMP",
  4:"IPRP",
  5:"POO",
  6:"PPP",
  7:"RC",
  8:"SI",
  9:"SO",
  10:"TC",
  11:"TI",
  12:"ES",
};

function TestList({ selectedTag, searchQuery }) {
  const [testsToSolve, setTestsToSolve] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const payload = await DataFetchGet('api/REQ5/choose-test/', null);
        setTestsToSolve(payload.data.tests || []);
        if (!payload.data.tests || payload.data.tests.length === 0) {
          Popup.create({
            title: null,
            content: "You have no tests to solve!",
            buttons: {
              right: [{
                text: 'Ok',
                key: 'ctrl+enter',
                action: function () {
                  Popup.close();
                  window.location.href = "..";
                }
              }]
            }
          });
          setTimeout(() => {
            Popup.close();
            window.location.href = "..";
          } , 7000);
        }
      } catch (error) {
        console.error('Error fetching tests:', error);
      }
    };

    fetchData();
  }, []);

  const testChosenAction = (testId) => {
    window.location.href = `/solve-test/${testId}`;
  };

  const filteredTests = testsToSolve.filter((item) => {
    const matchesTag =
      selectedTag === 0 || selectedTag === undefined
        ? true
        : item.tags && item.tags.includes(tagsLabels[selectedTag]);

    const matchesSearch =
      searchQuery === '' ||
      item.title.toLowerCase().includes(searchQuery.toLowerCase());

    return matchesTag && matchesSearch;
  });

  return (
    <div className='tests-box'>
      {filteredTests.map((item) => (
        <div key={item.id} onClick={() => testChosenAction(item.id)} className="chooseTest_box">
          <b>{item.title}</b><br />
          <div className="tags">
            {item.tags && item.tags.map((item2) => (
              <p key={item2} className="ChooseTest_tag">{item2}</p>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

export default ChooseTest;
