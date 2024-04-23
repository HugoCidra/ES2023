import React from 'react'
import Login from './Login/Login';
import Home from './Home_Page/Home';
import CreateQuizz from './Create_Quiz/CreateQuizz';
import ReviewQuizz from './Review_Quiz/ReviewQuizz';
import CreateTest from './Create_Test/CreateTest';
import SolveTest from './Solve_Test/SolveTest';
import ChooseTest from './Choose_Test/ChooseTest';
import Profile from './Profile/Profile';
import Admin from './Admin/Admin'; 
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Popup from 'react-popup';

/**
 * Main component of the programn.
 * Each route will connect to another component with a router.
 * @returns {html} The main site
 */

function App() {
  return (
    <Router>
      <Popup />
      <div className= "App">
        <div className= "content">
            <Routes>
              <Route path= '/' element={<Home/>}></Route>
              <Route path= '/login' element={<Login type='login'/>}></Route>
              <Route path= '/register' element={<Login type='register'/>}></Route>
              <Route path= '/create-quizz' element={<CreateQuizz/>}></Route>
              <Route path= '/create-quizz/:id' element={<CreateQuizz/>}></Route>
              <Route path= '/review-quizz' element={<ReviewQuizz/>}></Route>
              <Route path= '/solve-test/:id' element={<SolveTest/>}></Route>
              <Route path= '/choose-test' element={<ChooseTest/>}></Route>
              <Route path= '/profile' element={<Profile/>}></Route>
              <Route path= '/admin' element={<Admin/>}></Route>
              <Route path= '/create-test' element={<CreateTest/>}></Route>
            </Routes>
        </div>
      </div>
    </Router>

  );
}

export default App;
