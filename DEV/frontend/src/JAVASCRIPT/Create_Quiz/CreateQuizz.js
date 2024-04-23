import React, { useEffect, useState } from "react";
import "../../IMAGES/Logo.png";
import "../../IMAGES/Icon.png";
import "./Create_Quizz.css"
import "../Review_Quiz/button.css";
import '../index.css';
import DataFetchPost from "../../DataFetchFunctions/DataFetchPost";
import DataFetchGet from "../../DataFetchFunctions/DataFetchGet";
import { useParams } from "react-router-dom";
import NavBar from '.././NavBar/NavBar';
import Popup from 'react-popup';
import Select from 'react-select'

/**
 * Function to check if there are repeated options.
 * @param {Array} listOptions - List of answer options.
 * @returns {boolean} - Returns true if there are repeated options, otherwise false.
 */

function popups(message) {
  Popup.create({
    title: null,
    content: message,
    buttons: {
        right: [{
            text: 'Ok',
            key: 'ctrl+enter',
            action: function () {
                window.location.href = '/';
              }
          }]
      }
  });
  setTimeout(() => { 
    Popup.close();
    window.location.href = "/";
  }, 7000);
}

function cancel_popup() {
  Popup.create({
    title: null,
    content: 'Are you sure you want to leave?',
    buttons: {
        right: [{
            text: 'Yes',
            key: 'ctrl+enter',
            action: function () {
                Popup.close();
                window.location.href = '/';
                return;
              }
          },
          {
            text: 'Cancel',
            key: 'esc',
            action: function () {
              Popup.close();
              return;
            }
          }]
      }
  });
  setTimeout(() => { 
    Popup.close();
  }, 7000);
}

function spell_popup(msg, question_id, body, options, opt_text, tags) {
  Popup.create({
    title: null,
    content: msg + " Submit anyway?",
    buttons: {
        right: [{
            text: 'Yes',
            key: 'ctrl+enter',
            action: function () {
              button_submit(body, options,opt_text, tags,question_id, false);

              Popup.close();
              return;
            }
          },
          {
            text: 'Cancel',
            key: 'esc',
            action: function () {
              Popup.close();
              return;
            }
          }]
      }
  });
  // setTimeout(() => { 
  //   Popup.close();
  // }, 5000);
}

function repeatOption(listOptions) {
  if (listOptions.length<6) return;
  for (let i=0;i<listOptions.length;i++){
    for (let a=0;a<listOptions.length;a++){
      if(a!==i){
        if (listOptions[i].body===listOptions[a].body){
          //alert("ERROR: Repeated answer options")
          Popup.alert("ERROR: Repeated answer options");
          setTimeout(() => {
            Popup.close();
          } , 7000);
          return true;
        }
      }
    }
  }
  return false;
}

/**
 * Function to validate if the input contains valid characters.
 * @param {string} inputValid - The input string to validate.
 * @returns {boolean} - Returns true if the input contains valid characters, otherwise false.
 */

function characterInput(inputValid) {
    var characters = /[A-Za-z0-9?!.+-_,: '$*&#]+$/
    if (inputValid.match(characters)) {
    // alert("Quiz Submitted!");
    return true;}
    else if (inputValid.length===0) return true;
    else {
    //alert("Please input valid characters.");
    Popup.alert("Please input valid characters.");
    setTimeout(() => {
      Popup.close();
    } , 7000);
    console.log("Please input valid characters.")
    return false;
  }
}

/**
 * Function to validate if a question has been submitted.
 * @param {string} iQuestao - The question input.
 * @returns {boolean} - Returns true if a question has been submitted, otherwise false.
 */

function questao(iQuestao) {
  if(iQuestao.length===0) {
      //alert('ERROR: You have to submit your question.');
      Popup.alert('ERROR: You have to submit your question.');
      setTimeout(() => {
        Popup.close();
      } , 7000);
      return false;
  } else {
    return true;
  }
}

/**
 * Function to validate if a justification has been submitted.
 * @param {string} explicacao - The justification input.
 * @returns {boolean} - Returns true if a justification has been submitted, otherwise false.
 */

function justification(explicacao) {
  if(explicacao.length===0) {
      //alert('ERROR: You have to submit your justification.');
      Popup.alert('ERROR: You have to submit your justification.');
      setTimeout(() => {
        Popup.close();
      } , 7000);
      return false;
  } else {
    return true;
  }
}

/**
 * Function to ensure exactly one option is marked as correct.
 * @param {Array} options - List of answer options.
 * @returns {boolean} - Returns true if exactly one option is marked as correct, otherwise false.
 */

function chooseCorrect(options){
  let contador=0;
  if (options.length<6) return;
  for (let i=0;i<options.length;i++){
    if (options[i]["is_correct"]===true) contador+=1;
  }
  if(contador!==1){
    //alert('ERROR: You have to choose a unique correct option')
    Popup.alert('ERROR: You have to choose a unique correct option');
    setTimeout(() => {
      Popup.close();
    } , 7000);
    return false;
  }
  else return true;
}

/**
 * Function to validate if exactly six options have been submitted.
 * @param {Array} inputOption - List of answer options.
 * @returns {boolean} - Returns true if exactly six options have been submitted, otherwise false.
 */

function sixOptions(inputOption) {
  if(inputOption.length<6) {
    //alert("ERROR: You have to submit six options");
    Popup.alert("ERROR: You have to submit six options");
    setTimeout(() => {
      Popup.close();
    } , 7000);
    return false;
  }
  for (let i = 0; i < 6; i++) {
    if(inputOption[i].body==="") {
        //alert("ERROR: You have to submit six options");
        Popup.alert("ERROR: You have to submit six options");
        setTimeout(() => {
          Popup.close();
        } , 7000);
        return false;
      } 
  }
  return true;
}


/**
 * Function to save quiz data via a POST request.
 * @param {string} body - The question input.
 * @param {Array} options - List of answer options.
 * @param {string} opt_text - The optional text input.
 * @param {string} tags - The selected tags.
 * @param {number} question_id - The question ID.
 */

async function button_save(body, options,opt_text, tags,question_id) {
  let result = await DataFetchPost("api/REQ3/save-quiz", {
      question_id: question_id,
      body: body,
      options: options,
      explanation: "explanation",
      opt_text: opt_text,
      tags:tags
  });
  console.log(result);
}

/**
 * Function to submit quiz data via a POST request.
 * @param {string} body - The question input.
 * @param {Array} options - List of answer options.
 * @param {string} opt_text - The optional text input.
 * @param {string} tags - The selected tag.
 * @param {number} question_id - The question ID.
 * @returns {Promise<boolean>} - Returns a promise that resolves to true if the quiz data is submitted successfully, otherwise false.
 */

async function button_submit(body, options,opt_text, tags,question_id, check) {
  if(questao(body) && !repeatOption(options) && sixOptions(options) && chooseCorrect(options)) {
    if (tags.length===0){
      //alert("ERROR: You need to choose at least one tag")
      Popup.alert("ERROR: You need to choose at least one tag");
      setTimeout(() => {
        Popup.close();
      } , 7000);
      return false;
    }

    let result = await DataFetchPost("api/REQ3/submit-quiz", {
      question_id: question_id,
      body: body,
      options: options,
      explanation: "",
      opt_text: opt_text,
      tags:tags,
      check:check
    });

    // check if the substring mispelled is in result.data.message
    
    if (result.success==="yes" && result.data.status===400){
      //alert("ERROR: " + result.data.message)
      if (!result.data.message.includes("misspelled")) {
        Popup.alert("ERROR: " + result.data.message);
        setTimeout(() => {
          Popup.close();
        } , 5000);
      }
      else {
        spell_popup("ERROR: " + result.data.message, question_id, body, options, opt_text, tags, check);
      }
      return false;
    }
    else {
      popups("Quiz Submitted!");
      return true;
    }

  }
  else return false;
}

/**
 * Component to manage saved and submitted messages.
 * @param {string} body - The question input.
 * @param {Array} options - List of answer options.
 * @param {string} opt_text - The optional text input.
 * @param {string} tag - The selected tag.
 * @param {number} question_id - The question ID.
 * @returns {JSX.Element} - Returns a JSX element for managing saved and submitted messages.
 */

const Botao = (body, options,opt_text, tags,question_id, editable) => {
  const [state, setState] = useState({
    showMessageSaved: false,
    showMessageSubmitted: false,
  });


/**
  * Event handler for the "SAVE" button click. It saves quiz data and shows a "Quiz Saved" message.
  */

  function onButtonClickHandler1() {
    button_save(body, options,opt_text, tags, question_id);
    setState({ showMessageSaved: true });

    popups("Quiz Saved!");
    
  }

/*
  Calls the function to submit the quiz data and handles the result
*/

  function onButtonClickHandler2() {
    button_submit(body, options,opt_text, tags,question_id, true);
    }  
  return (
    <div>
      <div className="container_para_botoes_save_submit_cancel">

        { editable && <button className="button-default cbutton" onClick={cancel_popup}>Cancel</button> }

        { !editable && <button className="button-default cbutton" onClick={() => {window.location.href = '/';}} >Back</button> }

        { editable && <button className="button-default cbutton" onClick={onButtonClickHandler1}>Save</button> }

        { editable && <button className="button-default cbutton" onClick={onButtonClickHandler2}>Submit</button> }
      </div>
    </div>
  );
};


/**
 * Component to handle and render a question input field.
 *
 * @param {string} body - The current value of the question input.
 * @param {function} setBody - A function to set the value of the question input.
 *
 * @returns {JSX.Element} - Returns a JSX element representing the question input field.
 */

const Question = (body, setBody, editable) => {
   
  /**
   * Handles the change in the question input field and sets the question body.
   *
   * @param {Event} e - The event object representing the change in the input field.
   */

  function handleQuestion(e) {
    if (characterInput(e.target.value)) {       //Validates and sets the question body
      setBody(e.target.value);
    }
  }
  return (
    <div className="ext-boxP">
      {/*--------FIELD PARA PERGUNTA--------*/}
        <textarea className="boxP"
          type="text"
          name="question"
          id="question"
          placeholder="What's your question?"
          required=""
          value = {body}
          onChange={(e) => handleQuestion(e)}
          readOnly={!editable}
        />
    </div>
  );
};

/**
 * Component to handle each option input.
 * @param {Array} options - List of answer options.
 * @param {function} setOptions - Function to set the list of answer options.
 * @param {number} id - The option ID.
 * @param {boolean} newQuestion - Indicates whether it's a new question.
 * @returns {JSX.Element} - Returns a JSX element for handling each option input.
 */

const Option = (options,setOptions,id,newQuestion,editable) => {
  const [option,setOption]=useState({id:id,body:"",is_correct:false,justification:""})
  useEffect(()=>{
      //Load quiz option data
      if(newQuestion===false){
        if(options[id-1]!==undefined){
          let option_={};
          option_.id=id
          option_.body=options[id-1].body
          option_.is_correct=options[id-1].is_correct
          option_.justification=options[id-1].justification
          setOption(option_)
          options[id-1]=option_;
        }
      }
      else options[id-1]=option;
},[newQuestion,id,options])

/**
 * Handles the change in the option's body and updates the options list.
 *
 * @param {Event} e - The event object representing the change in the input field.
 */

  function handleChangeOption(e) {
    let option_={id:option.id,body:e.target.value,is_correct:option.is_correct,justification:option.justification}
    setOption({id:option.id,body:e.target.value,is_correct:option.is_correct,justification:option.justification})
    if (characterInput(e.target.value)) {
      let options_ = options
      options_[id - 1] = option_;
      setOptions(options_)
    } 
  }


  /**
 * Handles the change in the option's correctness state and updates the options list.
 *
 * @param {Event} e - The event object representing the change in the checkbox state.
 */

  function checkbox(e) {
    let option_={id:option.id,body:option.body,is_correct:e.target.checked,justification:option.justification}
    setOption({id:option.id,body:option.body,is_correct:e.target.checked,justification:option.justification})
    for (let i=0;i<options.length;i++){
      if(i!==id-1){
        if(options[i].is_correct===true) options[i].is_correct=false;
      }
    }
    let options_ = options;
    options_[id - 1]=option_
    setOptions(options_);
  }


/**
 * Handle change in the justification for an option.
 * @param {Event} e - The event object from the input field.
 * @returns {JSX.Element}
 */

  function handleChangeJustification(e){
    let option_={id:option.id,body:option.body,is_correct:option.is_correct,justification:e.target.value}
    setOption({id:option.id,body:option.body,is_correct:option.is_correct,justification:e.target.value})
    let options_ = options
    options_[id - 1] = option_;
    setOptions(options_)
  }

  return (
    <div className="option-container">
      {/*--------FIELD PARA RESPOSTA COM CHECKBOX--------*/}
      <div className="container-create-quizz">
        <input
          type="text"
          id="option"
          placeholder={`Option ${id}`}
          required=""
          value = {option.body}
          onChange={(e) => handleChangeOption(e)}
          maxLength="512"
          readOnly={!editable}
        />
        <div className="choice-prefix-create-quizz">
          <input
            type="radio"
            name="1"
            id="check"
            required=""
            checked={option.is_correct}
            onChange={(e) => {
                if (editable)
                  checkbox(e);
              }}
          />
        </div>
      </div>

    <div className="container-create-quizz" >
      
     {/*  <textarea className="justif-create-quizz" placeholder="Justification"></textarea> */}
        <textarea
          type="textarea"
          placeholder={`Justification`}
          required=""
          value={option.justification}
          onChange={(e) => handleChangeJustification(e)}
          maxLength="512"
          readOnly={!editable}
        />
        
    </div>
    </div>
  );
};

/**
 * Component to handle the optional text input.
 * @param {string} opt_text - The optional text input.
 * @param {function} setOpt_text - Function to set the optional text input.
 * @returns {JSX.Element} - Returns a JSX element for handling the optional text input.
 */

const Explanation = (opt_text,setOpt_text,editable) => {  
  function handleExplanationInput(e) {
    if (characterInput(e.target.value)) {
      setOpt_text(e.target.value);
    }
  }
  return (
    <div className="ext-boxP">
        <input className="boxP"
          type="text"
          name="justification"
          placeholder="Optional Text" 
          required=""
          value= {opt_text}
          onChange={(e) => handleExplanationInput(e)}
          readOnly={!editable}
        />
    </div>
  );
};

/**
 * Component to render an input field for reviewer justification.
 * @param {string} text - The reviewer justification text.
 * @returns {JSX.Element} - Returns a JSX element for rendering the input field for reviewer justification.
 */

const Explanation_Reviewer = (text) => {  
  return (
        <li className="reviewer-justificacao">{text}</li>
  );
};

/**
 * Component to handle tags dropdown.
 * @param {string} tag - The selected tag.
 * @param {function} setTag - Function to set the selected tag.
 * @returns {JSX.Element} - Returns a JSX element for handling tags dropdown.
 */

const Tags = (tag,setTag,editable)=>{
  const [tags,setTags]=useState([])
  useEffect(()=>{
    async function a (){
      try {
        //buscar tags
        const response = await DataFetchGet('api/REQ6/tags/', null);
        let tags_=response.data.tags;
        if(tags_.length===0){
          setTags(["-1"])
          setTag("-1")
        }
        else {setTags(tags_);}
    } catch (error) {
        setTags(["-1"])
        setTag("-1")
    }}
    a();
  },[setTag])

  function tagHandler(e){
    setTag(e.map((i)=>{
      return i.value}));
  }

  const options = tags.map(item => {
    return ({value:item, label:item})
  })

  const customStyles = {
    control: (provided, state) => { 
      if (state.isFocused) {
        return {...provided, borderColor: '#3FA9F5', boxShadow: 'none',
        ':hover': {borderColor: '#3FA9F5', boxShadow: '0 0 0 1px #3FA9F5'},    
      }
      }
      return provided;
    },
    multiValueRemove: (provided, state) => ({ ...provided,
      color: 'rgb(221,189,189)',
      ':hover': {backgroundColor: 'rgb(221,189,189)', color: 'rgb(221,189,189)'},
    }),
    option: (provided, state) => ({...provided, backgroundColor : 'white',
        ':hover': {backgroundColor: '#3FA9F5', boxShadow: '0 0 0 1px #3FA9F5'},    
    }),
  };

  return (
        <Select placeholder="Select Tags"
          closeMenuOnSelect={false}
          value={options.filter(obj => tag.includes(obj.value))}
          isMulti
          onChange={(e) => { tagHandler(e) }}
          options={options}
          styles={customStyles}
          isDisabled={!editable}
        />
  )
}

/**
 * CreateQuizz component.
 * @returns {JSX.Element} - Returns a JSX element for the CreateQuizz component.
 */

const CreateQuizz = () => {
  const id = parseInt(useParams().id);
  const [reviewJustifications,setReviewJustifications]=useState([])
  const [body, setBody] = useState("");
  const [options, setOptions] = useState([]);
  const [opt_text, setOpt_text] = useState("");
  const [question_id, setQuestion_id] = useState(0);
  const [tags,setTags]=useState([]);
  const [newQuestion,setNewQuestion]=useState(true);

  const [editable,setEditable]=useState(true);

  useEffect(()=>{
    if(isNaN(id))console.log("New Quizz")
    else {
      console.log("Quizz Existente")
      DataFetchGet(`api/REQ3/get-quiz/${id}`).then((value)=>{
        let data = value["data"]["data"]
        if (value.success==="no"){
          //alert("ERROR: DataBase is not connected");
          Popup.alert("ERROR: DataBase is not connected");
          setTimeout(() => {
            Popup.close();
          } , 7000);
          setTimeout(()=>{window.location.href = "/"},1000)
        }
        else if (data.status===404) {
          //alert(`ERROR: ${data["message"]}`)
          Popup.alert(`ERROR: ${data["message"]}`);
          setTimeout(() => {
            Popup.close();
          } , 7000);
          setTimeout(()=>{window.location.href = "/"},1000)
        }
        
        else if (value.success==="yes"){
          if (data.state === 2 || data.state === 4)
            setEditable(false);

          console.log(data)
          setOptions(data.options)
          setBody(data.question)
          setTags(data.tags)
          setOpt_text(data.opt_text)
          setQuestion_id(id)
          setNewQuestion(false)
          setReviewJustifications(data.rejected_justifications);
        }
        })
        }
},[id])

  return (
    <div>
      <NavBar/>
      <div className='quiz-title'>
      <div className='quiz-title-text'>
        {Question(body,setBody,editable)}
        {Tags(tags,setTags,editable)}
      </div>
      <div className="line"/>
      {Explanation(opt_text,setOpt_text,editable)}
      </div>
      <div className="grid-container-quizz">
        {Option(options,setOptions,1,newQuestion,editable)}
        {Option(options,setOptions,2,newQuestion,editable)}
        {Option(options,setOptions,3,newQuestion,editable)}
        {Option(options,setOptions,4,newQuestion,editable)}
        {Option(options,setOptions,5,newQuestion,editable)}
        {Option(options,setOptions,6,newQuestion,editable)}
      </div>
      {Botao(body, options,opt_text, tags,question_id, editable)}
      {reviewJustifications.length>0  && <div className="justification-reviewer">
      <h2>Review Justifications</h2>
      <div className="line"></div>
      {reviewJustifications.map((item)=>{
        return Explanation_Reviewer(item.justification)})}
      </div>}
    </div>
  );
};
export default CreateQuizz;
