import React from "react";
import "../index.css";
import "./SolveTest.css";
import RadioButton from "./RadioButton/RadioButton";
import DataFetchGet from "../../DataFetchFunctions/DataFetchGet";
import DataFetchPost from "../../DataFetchFunctions/DataFetchPost";
import NavBar from ".././NavBar/NavBar";
import Popup from 'react-popup';

/**
 * Global variables.
 */
var global = {};
var grade_results = {};
var submitted = false;

/**
 * Represents individual quiz questions.
 * @extends React.Component
 */
class Quiz extends React.Component {
  /**
   * Render the question text, associated options, and potential justification when submitted.
   * @returns {JSX.Element} Rendered component.
   */

  state = {
    RespostaSelecionadaID: global.solutions[this.props.data.id],
    ClassResultName: this.option_classname(),
  };

  setOption(event) {
    console.log(event.target.value);
    global.solutions[this.props.data.id] = event.target.value;
  }

  radioChangeHandler = (event) => {
    this.setState({
      RespostaSelecionadaID: event.target.value,
    });
    global.solutions[this.props.data.id] = event.target.value;
  };

  /**
   * Define class names for option based on its state.
   * @returns {string} The class name string.
   */
  option_classname(optid, selecionada) {
    let ret = "";
    if (submitted === true) {
      ret = "submitted ";
      if(selecionada) ret+= " solve_test_selecionada";
      if (optid === grade_results.results[this.props.data.id].correct) {
        ret += " solve_test_correto";
      } else if (
        optid != grade_results.results[this.props.data.id].correct &&
        selecionada === true
      ) {
        ret += " solve_test_errado";
      }
    }

    return ret;
  }

  render() {
    return (
      <>
        <div className="box">{this.props.data.body}</div>
        <div className="contagem-quiz">
          {this.props.index + 1}/{this.props.perguntas}
        </div>
        <div className="questions_justification">
        <div className="grid-container">
          <div className={"radio-toolbar"}>
            {this.props.data.opts.map((opts) => (
              <RadioButton
                classe={this.option_classname(
                  opts.id,
                  this.state.RespostaSelecionadaID == opts.id
                )}
                changed={this.radioChangeHandler}
                id={opts.id}
                isSelected={this.state.RespostaSelecionadaID == opts.id}
                label={opts.body}
                value={opts.id}
                key={opts.id}
                disabled={submitted}
              />
            ))}
          </div>
        </div>
        {submitted === true &&
          grade_results &&
          grade_results.results &&
          this.props.data.id in grade_results.results && (
            <div className="box" id="justification_box">
              Justification:{" "}
              {grade_results.results[this.props.data.id].justification}
            </div>
            
          )}
          </div>
        {/* (submitted === true && this.props.data.id in grade_results.results) && <div className="box pergunta" id="justification_box" >Justification: {grade_results.results[this.props.data.id].justification}</div> */}
      </>
    );
  }
}

/**
 * Buttons component for test submission and navigation.
 * @extends React.Component
 */
class Buttons extends React.Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

    /**
     * Handle test submission.
     * @param {Event} event - The triggered event.
     */
    async handleSubmit(event) {
        let data_post = JSON.stringify(global);

        await DataFetchPost(`api/REQ5/grade_test/`, data_post).then((result) => {
            let data = result.data;
            if (data['status'] === 501) {
                console.log(data['log']);
                Popup.alert("You've already done this test!");
                setTimeout(() => {
                    Popup.close();
                  }, 7000);
                  window.location.href = "..";
                return;
            } else if (data['status'] === 500) {
                window.location.href = "/login";
                Popup.alert(data['log']);
                setTimeout(() => {
                    Popup.close();
                }, 7000);
                return;
            }

      console.log(result);
      grade_results = data;
      window.scrollTo(0, 0);
      submitted = true;
      this.props.rerender();
    });

    event.preventDefault();
  }

  /**
   * Handle navigation or cancel actions.
   * @param {Event} event - The triggered event.
   */
  async handleCancel(event) {
    //if (window.confirm("Are you sure you want to go to homepage?")) {
    //  window.location.href = "..";
    //}
    Popup.create({
      title: null,
      content: (submitted !== true) ? 'Are you sure you want to go to homepage? You will lose your progress.' : 'Are you sure you want to go to homepage?',
      buttons: {
        right: [{
          text: 'yes',
          className: 'normal',
          action: function () {
            Popup.close();
            window.location.href = "..";
          }
        },{
          text: 'No',
          className: 'danger',
          action: function () {
            Popup.close();
          }
        }]
      }
    });
    event.preventDefault();
  }

  /**
   * Render different button states based on test completion.
   * @returns {JSX.Element} Rendered component.
   */
  render() {
    return (
      <>
        <div className="container_points">
          {submitted === true && (
            <>            
            <h2 className="manypoints">
              YOU GOT {grade_results.grade} POINTS
            </h2>
            <button className="button-default" onClick={this.handleCancel}>
              HOMEPAGE
            </button>
            </>
 
             
          )}
        </div>
        
       
        
        <div className="container_solve_test_buttons">
          {submitted === false && (
            <button className="button-default" onClick={this.handleSubmit}>
              SUBMIT
            </button>
          )}

          {submitted === false && (
            <button className="button-default" onClick={this.handleCancel}>
              CANCEL
            </button>
          )}
        </div>
      </>
    );
  }
}

/**
 * Main component for the quiz/test interface.
 * @extends React.Component
 */
class SolveTest extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      questions: [], // Initially empty, will be populated from API
      currentQuestionIndex: 0, // Keep track of the current question
    };
    this.handleNextQuestion = this.handleNextQuestion.bind(this);
    this.handlePreviousQuestion = this.handlePreviousQuestion.bind(this);
    this.rerender = this.rerender.bind(this);
  }

  handleNextQuestion() {
    this.setState((prevState) => ({
      currentQuestionIndex: Math.min(
        prevState.questions.length - 1,
        prevState.currentQuestionIndex + 1
      ),
    }));
  }

  handlePreviousQuestion() {
    this.setState((prevState) => ({
      currentQuestionIndex: Math.max(0, prevState.currentQuestionIndex - 1),
    }));
  }

  /**
   * Force a re-render of the component.
   */
  rerender() {
    this.setState(this.state);
  }

  /**
   * Fetch the test data on component mount.
   */
  async componentDidMount() {
    let currentUrl = JSON.stringify(window.location.href);
    let lastSlash = currentUrl.lastIndexOf("/");
    let test_id = currentUrl.slice(lastSlash + 1, -1);
    test_id = parseInt(test_id);
    let temp = { id: test_id };

        await DataFetchGet(`api/REQ5/get_test/`, temp).then((result) => {
            let data = result.data;
            if (data['status'] === 401) {
                console.log(data['log']);
                return;
            } else if (data['status'] === 500) {
                window.location.href = "/login";
                Popup.alert(data['log']);
                setTimeout(() => {
                    Popup.close();
                }, 7000);
                return;
            }
            global = temp;
            let solutions = {};
            for (let i = 0; i < result.data.questions.length; i++) {
                solutions[result.data.questions[i].id] = -1;
            }
            global["solutions"] = solutions;

      this.setState(result.data);
    });
  }

  /**
   * Render the quiz and associated components.
   * @returns {JSX.Element} Rendered component.
   */
  render() {
    const { currentQuestionIndex, questions } = this.state;
    return (
      <>
        <main>
          <NavBar />
          <div className="container_solve_test">
            {questions.length > 0 && (
              <>
                <div className="navigation-buttons">
               
                  <button
                    className={`arrow-button left ${
                      currentQuestionIndex === 0 ? "disabled" : ""
                    }`}
                    onClick={this.handlePreviousQuestion}
                    disabled={currentQuestionIndex === 0}
                  >
                    {/* This is the left arrow */}
                  </button>
                
                  <Quiz
                    selecionada={global.solutions[this.props.id]}
                    data={questions[currentQuestionIndex]}
                    key={questions[currentQuestionIndex].id}
                    perguntas={questions.length}
                    index={currentQuestionIndex}
                  />
                  <button
                    className={`arrow-button right ${
                      currentQuestionIndex === questions.length - 1
                        ? "disabled"
                        : ""
                    }`}
                    onClick={this.handleNextQuestion}
                    disabled={currentQuestionIndex === questions.length - 1}
                  >
                    {/* This is the right arrow */}
                  </button>
                 
                </div>
                <Buttons rerender={this.rerender}></Buttons>
              </>
            )}
           
          </div>
        </main>
      </>
    );
  }
}

/** @module SolveTest */
export default SolveTest;
