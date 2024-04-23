/**
 * Import CSS stylesheets
 */
import './button.css';
import './style.css';
import '../index.css';


/**
 * Import React and other components
 */
import React from 'react'
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';
import Popup from 'react-popup';

/**
 * Initialize a variable for acceptance
 * @type {number}
 */
var acceptance = 2;

/**
 * Define a React component for displaying a question
 * @class
 */
class Question extends React.Component {
    /**
     * Render the Question component.
     * @returns {JSX.Element}
     */
    render() {
        return <div className="question boxRQ">{this.props.text}</div>
    }
}

/**
 * Define a React component for displaying answer choices.
 * @class
 */
class AnswersContainer extends React.Component {
    /**
     * Render the AnswersContainer component.
     * @returns {JSX.Element}
     */
    
    render () {
        return  <>
                    <div className="options_container boxRQ">
                            <ChoiceContainerReview is_correct = {this.props.option1[2]} body={this.props.option1[0]} text={this.props.option1[1]} />
                            <ChoiceContainerReview is_correct = {this.props.option2[2]} body={this.props.option2[0]} text={this.props.option2[1]} />
                            <ChoiceContainerReview is_correct = {this.props.option3[2]} body={this.props.option3[0]} text={this.props.option3[1]} />
                            <ChoiceContainerReview is_correct = {this.props.option4[2]} body={this.props.option4[0]} text={this.props.option4[1]} />
                            <ChoiceContainerReview is_correct = {this.props.option5[2]} body={this.props.option5[0]} text={this.props.option5[1]} />
                            <ChoiceContainerReview is_correct = {this.props.option6[2]} body={this.props.option6[0]} text={this.props.option6[1]} />       
                    </div>
                </>
    }

}

/**
 * Define a React component for displaying answer choices.
 * @class
 */
class ChoiceContainerReview extends React.Component {
    /**
    * Render the ChoiceContainerReview component.
    * @returns {JSX.Element}
    */
    constructor(props) {
         super(props);
        }
   render() {
       return <div className="option_container">
               <div className={this.props.is_correct === true ? "body_container correto":"body_container"}>{this.props.body}</div>
               <textarea className=" justif_container " readOnly disabled>{this.props.text}</textarea>
       </div>
   }
}

/**
 * Define a React component for accepting and rejecting questions
 * @class
 */
class ButtonsAccRej extends React.Component {
    
    constructor() {
        super();
         /**
         * Event handler for accepting a question
         * @param {Event} event - The click event
         */
        this.handleSubmitAcc = this.handleSubmitAcc.bind(this);
         /**
         * Event handler for rejecting a question
         * @param {Event} event - The click event
         */
        this.handleSubmitRej = this.handleSubmitRej.bind(this);
    }

    // Event handler for accepting a question
    handleSubmitAcc (event) {
        if (acceptance === 2) {
            acceptance = 1;
            event.target.className="button-default accept_review_click";
        } else if (acceptance === 0) {
            acceptance = 1;
            event.target.className="button-default accept_review_click";
            this.reject_button.className="button-default reject_review";
        } else if (acceptance === 1) {
            acceptance = 2;
            event.target.className="button-default accept_review";
        }
        console.log(acceptance);
        
        event.preventDefault(); // Prevent the default button behavior
    }

    // Event handler for rejecting a question
    handleSubmitRej (event) {
        if (acceptance === 2) {
            acceptance = 0;
            event.target.className="button-default reject_review_click";
        } else if (acceptance === 1) {
            acceptance = 0;
            event.target.className="button-default reject_review_click";
            this.accept_button.className="button-default accept_review";
        } else if (acceptance === 0) {
            acceptance = 2;
            event.target.className="button-default reject_review";
        }
        console.log(acceptance);
    }

    /**
     * Render the ButtonsAccRej component.
     * @returns {JSX.Element}
     */
    render() {
        return <div className="container_for_button_acc_rej">
            <button className="button-default accept_review" ref={ref => this.accept_button = ref}  onClick={this.handleSubmitAcc}>ACCEPT</button>
            <button className="button-default reject_review" ref={ref => this.reject_button = ref}  onClick={this.handleSubmitRej}>REJECT</button>
        </div>
    }
}

/**
 * Define a React component for displaying the state of accepted and rejected questions
 * @class
 */
class BoxContainerState extends React.Component {
    /**
    * Render the BoxContainerState component.
    * @returns {JSX.Element}
    */
   render() {
       return <div className="boxRQ container_question_state">
           <div className="accepted">
               <p>Accepted</p>
               <p>{this.props.dataFromParent.accepted}/{this.props.dataFromParent.max_accepted}</p>
           </div>
           <div className="rejected">
               <p>Rejected</p>
               <p>{this.props.dataFromParent.rejected}/{this.props.dataFromParent.max_accepted}</p>
           </div>
       </div>
   }
}

/**
 * Define a React component for the justification
 * @class
 */
class JustificationContainer extends React.Component {
    
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.props.onChange(event);
    }

    /**
     * Render the JustificationContainer component.
     * @returns {JSX.Element}
     */
    render() {
        return <textarea maxLength="512" placeholder="Justification..." id= "justificationRQ" className="boxRQ justify_quiz_area" onChange={this.handleChange}></textarea>
    }
}

/**
 * Define a React component for submit and cancel buttons
 * @class
 */
class ButtonsCancelSubmit extends React.Component {

    constructor(props) {
        super(props);
        this.onClick = props.onClick;

        this.onCancel = this.onCancel.bind(this);
    }


    /**
 * Event handler for the cancel button.
 */
    
    onCancel = () => {
        // Display a confirmation dialog
        //const isConfirmed = window.confirm("Are you sure you want to leave this page? Your work will be lost.");

        // If the user confirms, navigate to the home page
        //if (isConfirmed) {
        //    window.location.href = '/';
        //}


    Popup.create({
        title: null,
        content: 'Are you sure you want to leave this page? Your work will be lost.',
        buttons: {
            right: [{
                text: 'Yes',
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
            }, {
                text: 'Cancel',
                className: 'danger',
                key: 'esc',
                action: function () {
                    Popup.alert('Operation Canceled');
                
                    /** Close this popup. Close will always close the current visible one, if one is visible */
                    Popup.close();
                }
            }]
        }
    });

    }

    /**
     * Render the ButtonsCancelSubmit component.
     * @returns {JSX.Element}
     */
    render() {
        return  <div className="container_submit_cancel">
                    <button className="button-default buttonRQ" id="submitRQ" onClick={this.onClick}>SUBMIT</button>
                    <button className="button-default buttonRQ" id="cancelRQ" onClick={this.onCancel}>CANCEL</button>
                </div>
    }
}

/**
 * Define a React component for the container Justification
 * @class
 */
class ContainerJustification extends React.Component {
    
    constructor(props) {
        super(props);

        this.state = {
            value: '',      // State to store justification text
            accepted: 2,     // 0 for rejected, 1 for accepted, 2 is the default value
        };
        
        /**
         * Event handler for text area changes
         * @param {Event} event - The change event
         */
        this.handleChange = this.handleChange.bind(this);

        /**
         * Event handler for submitting justifications
         * @param {Event} event - The click event
         */
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    // Event handler for text area changes
    handleChange(event) {
        this.setState({value: event.target.value });
    }
    
    // Event handler for submitting justifications
    async handleSubmit (event) {
        // Check if the acceptance status is still the default value (2)
        if (acceptance === 2) {
            Popup.alert("You must either accept or reject the question.");
            setTimeout(() => {
                Popup.close();
            } , 7000);
            return;
        } else if (acceptance === 0) {
            // Check justification length
            if (this.state.value.length < 40 || this.state.value.length > 512) {
                Popup.alert("Your justification must contain more than 40 and fewer than 512 characters.");
                setTimeout(() => {
                    Popup.close();
                } , 7000);
                return;
            }
        }
        // Update the accepted state
        this.setState({accepted: acceptance})
        
        // Log the data
        console.log(this.state);

        // Prepare data for a POST request
        let data_post = JSON.stringify({
            value: this.state.value,
            accepted: acceptance,
            id: this.props.id

        });

        // Log the data
        console.log(data_post);

        try {
            // Perform a data post request
            let result=await DataFetchPost('api/REQ4/vote/', data_post);
            console.log(result.data);
            window.location.href = '/review-quizz'; // Redirect to the home page
        } catch (error) {
            console.error(error.response.data);     // NOTE - use "error.response.data` (not "error")
        }

    }
    

    /**
     * Render the ContainerJustification component.
     * @returns {JSX.Element}
     */
    render(){
        return <>
            <JustificationContainer onChange={this.handleChange}/>
            <ButtonsCancelSubmit onClick={this.handleSubmit}/>
        </>
    }
}

// Export the components to be used in other parts of the application
export {ButtonsAccRej, BoxContainerState, ContainerJustification as ContainerJustificationSubmit, ChoiceContainerReview, AnswersContainer, Question };