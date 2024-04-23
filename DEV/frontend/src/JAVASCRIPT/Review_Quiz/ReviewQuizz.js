/**
 * Import necessary modules and CSS stylesheets
 */
import React, { useState, useEffect } from 'react';
import './button.css';
import './style.css';
import '../index.css';
import  {BoxContainerState, ContainerJustificationSubmit, AnswersContainer, Question, ButtonsAccRej} from './components';
import tab_logo from '../../IMAGES/Logo.png';
import icon from '../../IMAGES/Icon.png';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import NavBar from '.././NavBar/NavBar';
import Popup from 'react-popup';

/**
 * Define a React component for the Review Quiz page
 * @class
 */
class ReviewQuizz extends React.Component  {
  constructor(props) {
    super(props);
    this.state = {
      data: undefined
    }
  }

    /**
   * Lifecycle method that is called before the component mounts.
   * Fetches data from an API endpoint to get a question for review.
   * @async
   */
  async componentWillMount() {
    // Fetch data from an API endpoint to get a question for review
    let payload = await DataFetchGet('api/REQ4/quiz/', null);
    // Check the response status and update the component's state
    if (payload.data["status"] === 200) {
      this.setState(payload);
    } else {
      //Popup.alert("There are no questions for you to review at this time.");
      //setTimeout(() => {
        //  Popup.close();
        // }, 5000);
      //window.location.href = '/';
      Popup.create({
        title: null,
        content: 'There are no questions for you to review at this time.',
        buttons: {
            right: [{
                text: 'ok',
                key: 'ctrl+enter',
                action: function () {
                    // Passing true as the second argument to the create method
                    // displays it directly, without interupting the queue.
                    //Popup.create({
                    //    title: null,
                    //    content: 'I was configured to display right away, without affecting the queue. Closing this will display the previously visible popup.',
                    //    buttons: {
                    //        left: ['cancel'],
                    //        right: []
                    //    }
                    //}, true);
                    window.location.href = '/';
                }
            }]
        }
    });
    }
    
  }
 
   /**
   * Render the Review Quiz component.
   * @returns {JSX.Element}
   */
  render() {  
    // Check if data is undefined, which means there are no questions for review

    // if(this.debug){ //DEBUG ONLY!!!
    //   return <>
    //     <NavBar/>
    //     <div className="container_geral">
    //       <div className="container_left">
    //         <Question text = {this.sampleData.question} />
    //         <AnswersContainer option1 = {this.sampleData.options[0]} 
    //                           option2 = {this.sampleData.options[1]}
    //                           option3 = {this.sampleData.options[2]}
    //                           option4 = {this.sampleData.options[3]}
    //                           option5 = {this.sampleData.options[4]}
    //                           option6 = {this.sampleData.options[5]}/>
    //         <ButtonsAccRej/>
    //         </div>
    //       <div className="container_right">
    //         <BoxContainerState dataFromParent={{accepted: this.sampleData.accepted, rejected: this.sampleData.rejected, max_accepted:3}}/>
            
    //         <ContainerJustificationSubmit/>
    //       </div>
    //     </div>
    //   </>
    // }


    if(this.state.data === undefined){
      return <>
        <NavBar/>
      </>
    }else{
      
      return <>
      
        <NavBar/>
        <div className="container_geral">
          <div className="container_left">
            <Question text = {this.state.data.question} />
            <AnswersContainer option1 = {this.state.data.options[0]} 
                              option2 = {this.state.data.options[1]}
                              option3 = {this.state.data.options[2]}
                              option4 = {this.state.data.options[3]}
                              option5 = {this.state.data.options[4]}
                              option6 = {this.state.data.options[5]}/>
            <ButtonsAccRej/>
            </div>
          <div className="container_right">
            <BoxContainerState dataFromParent={{accepted: this.state.data.accepted, rejected: this.state.data.rejected, max_accepted:3}}/>
            
            <ContainerJustificationSubmit id={this.state.data.id}/>
          </div>
        </div>
      </>
    }
    }
  }
  
  export default ReviewQuizz;
  
