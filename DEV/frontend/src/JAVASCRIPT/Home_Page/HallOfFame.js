import React, { useState, useEffect } from 'react';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import './HallOfFame.css';
import '../index.css'
import SearchBar from "../SearchBar/SearchBar";

function HallOfFame() {
    const [creators, setCreators] = useState([[[]]]);
    const creatorRefs = creators.map(() => React.createRef());


    const [solvers, setSolvers] = useState([[[]]]);
    const SolverRefs = solvers.map(() => React.createRef());

    const [searchResults, setSearchResults] = useState([]);
    const [selectedCreatorIndex, setSelectedCreatorIndex] = useState(null);
    const [selectedSolverIndex, setSelectedSolverIndex] = useState(null);
    const [selectedUser, setSelectedUser] = useState('');

    const [isSearchFocused, setIsSearchFocused] = useState(false);
    const [blurTimeoutId, setBlurTimeoutId] = useState(null);

    

    useEffect(() => {
        async function fetchData() {
            try {
                const payloadCreators = await DataFetchGet('api/REQ2/creators/', null);
                console.log(payloadCreators);
                setCreators(payloadCreators.data.creators);


                const payloadSolvers = await DataFetchGet('api/REQ2/solvers/', null);

                console.log(payloadSolvers);


                setSolvers(payloadSolvers.data.solvers);


            } catch (error) {
                console.error(error);
            }
        }

        fetchData();
    }, []);


    const handleSearch = (searchTerm) => {
        console.log('HOF pesquisando por:', searchTerm);

        const results = creators.filter(user => 
            typeof user[0] === 'string' && user[0].toLowerCase().includes(searchTerm.toLowerCase())
        );
        setSearchResults(results);
    };

    const handleSelectUser = (user) => {
        setSelectedUser(user);
        setSearchResults([]);
        //find index returns -1 if not found... it can be used to show message
        const creatorIndex = creators.findIndex(u => u[0] === user);
        setSelectedCreatorIndex(creatorIndex);
        console.log(creatorIndex);
        const solverIndex = solvers.findIndex(u => u[0] === user);
        setSelectedSolverIndex(solverIndex);

        if (creatorIndex >= 3) {
            creatorRefs[creatorIndex].current.scrollIntoView({ behavior: 'smooth' ,block: 'nearest'});
        }
        if (solverIndex >= 3) {
            SolverRefs[solverIndex].current.scrollIntoView({ behavior: 'smooth' ,block: 'nearest'});
        }
        
    };

    return (
        <div className='HOF_body'>  
            
            <div className='HOF_tables_container'>
            <div className='HOF_tables'>
            <div className="HOF_field" id="HOFSolvers_field">
                <div className="HOFTitle_field" id="HOFTitleSolvers_field">
                    <div className="HOFTitles">Solvers</div>
                </div>
                <div className="HOFPodium_field">
                    <div className="HOFPodiumMedals_field">
                        <div className="HOFPodiumMedal1_field" ></div>
                        <div className="HOFPodiumMedal2_field" ></div>
                        <div className="HOFPodiumMedal3_field" ></div>
                    </div>
                    <div className="HOFPodiumUser_field">
                        {solvers.slice(0, 3).map((item,index) => (
                                <div className="HOF_user" key={item[0]}
                                    style={index === selectedSolverIndex ? {color: 'var(--click)', fontWeight: 'extra-bold'} : {}}>
                                    {item[0]} <div className="HOF_pontuation">{item[1]}</div>
                                </div>
                        ))}
                    </div>
                </div>
                <div className="HOFOtherUsers_field">
                    {solvers.slice(3).map((item, index) => (
                        <div ref={SolverRefs[index+3]}>
                            <div className="HOF_user" key={item[0]}
                                style={index === selectedSolverIndex-3 ? {color: 'var(--click)', fontWeight: 'extra-bold'} : {}}>
                                {`${index + 3}. ${item[0]}`} <div className="HOF_pontuation">{item[1]}</div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            <div className="HOF_field" id="HOFCreators_field">
                <div className="HOFTitle_field">
                    <div className="HOFTitles">Creators</div>
                </div>
                <div className="HOFPodium_field">
                    <div className="HOFPodiumMedals_field">
                        <div className="HOFPodiumMedal1_field" ></div>
                        <div className="HOFPodiumMedal2_field" ></div>
                        <div className="HOFPodiumMedal3_field" ></div>
                    </div>
                    <div className="HOFPodiumUser_field" >
                        {creators.slice(0,3).map((item, index) => (
                                <div className="HOF_user" key={item[0]} 
                                    style={index === selectedCreatorIndex ? {color: 'var(--click)', fontWeight: 'extra-bold'} : {}}>
                                    {item[0]} <div className="HOF_pontuation">{item[1]}</div>
                                </div>
                        ))}
                    </div>
                </div>
                <div className="HOFOtherUsers_field">
                    {creators.slice(3).map((item, index) => (
                        <div ref={creatorRefs[index+3]}>
                        <div className="HOF_user" key={item[0]}
                        style={index === selectedCreatorIndex-3 ? {color: 'var(--click)', fontWeight: 'extra-bold'} : {}}>
                            {`${index + 4}. ${item[0]}`} <div className="HOF_pontuation">{item[1]}</div>
                        </div>
                        </div>
                    ))}
                </div>
            </div>
            </div>
            </div>

            <div className='HOF_header'>
            <h1 className="HallOfFame_title">Hall of Fame</h1>
            <h2 className="HOF_SearchBar">
            <SearchBar
                value={selectedUser}
                onSearch={handleSearch}
                    onFocus={() => {
                    clearTimeout(blurTimeoutId);
                    setIsSearchFocused(true);
                    setSelectedUser('');
                }}
                onBlur={() => {
                    const timeoutId = setTimeout(() => {
                        setIsSearchFocused(false);
                    }, 200);
                    setBlurTimeoutId(timeoutId);
                }}
            />
            {isSearchFocused && searchResults.length > 0 &&(
                    <div className="HOFdropdown">
                        {searchResults.map(user => (
                            <button className='dropdownbutton' onClick={() => handleSelectUser(user[0])}>
                                {user[0]}
                            </button>
                        ))}
                    </div>
                )}</h2>
            </div>
            
        </div>
    );
}

export default HallOfFame;