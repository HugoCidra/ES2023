import React, {Component} from 'react';
import './Login_Register.css';
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost'
import DataFetchPut from '../../DataFetchFunctions/DataFetchPut';
import InputField from './Input_Field/Input_Field';


class Header extends Component {
    
    /**
     * Constructor for Header Component.
     * @param {String} title Title of the page
     */
    constructor () {
        super()
        this.title = "Login Page"
    }

    /**
     * Render function.
     * @returns {html.header} The logo of the site
     */
    render() {
        return(
            <header className='header'>
                <script>{window.localStorage.clear()}</script>
                <meta charSet="UTF-8" />
                <title>{this.title}</title>
                <link href={require("../../IMAGES/Icon.png")} rel="shortcut icon" type="img/png" />
                <meta content="width=device-width, initial-scale=1.0" name="viewport" />
                <link rel="stylesheet" href="../../CSS/Login_Register.css" />

                {/*---------------------------------------------LOGO---------------------------------------------*/}
                <div className='logo-div'>
                <img src={require("../../IMAGES/Logo.png")} alt="Logo" id="logo-login" />
                </div>
            </header>
        );
    }
}


class LoginForm extends Component {

    /**
     * Constructor for LoginForm Component.
     * ATTENTION!! IF CODE DOESNT WORK PLEASE REMOVE STATE FROM THE CONSTRUCTOR AND PUT IT OUTSIDE OF IT!!
     * @param {state} state Variable which holds information which may change during lifetime of this component
     * @param {String} username The username of the user
     * @param {String} password The password of the user
     * @param {String} log Message warning the user where to login if he has an account
     * @param {React.ref} logRef
     */
    constructor() {
        super()
        this.state = {
            username: '',
            password: '',
            log: '',
        }
        this.logRef = React.createRef()
    }

    /**
     * Sets the value of event as the username.
     * @param {String} event 
     */
    handleUsernameInput = event => {
        this.setState({username: event.target.value})
    }
    /**
     * Sets the value of event as the password.
     * @param {String} event 
     */
    handlePasswordInput = event => {
        this.setState({password: event.target.value})
    }
    /**
     * Sets the value of str as the log message with the color Red.
     * @param {String} str 
     */
    handleLogOutput = (str) => {
        this.logRef.current.style.color = "red"
        this.setState({log: str})
    }

    /**
     * Handles form submission.
     * @param {Event} event - The form submission event.
     */
    handleSubmit = event => {
        event.preventDefault(); // Prevents the default form submission behavior
        this.submit(this.state); // Calls the submit method with the current state
    };


    /**
     * Sends the values of the username and password to the DataBase and receives a value then redirect them to the main page.
     * Error handling in case the DataBase is unreachable.
     * @param {state} state State variable defined on the constructor
     * @returns If the value received is not 200 returns with an error
     */
    async submit(state){
        try{
            let a = await DataFetchPut('api/login/', {
                username: state.username,
                password: state.password
            })
            if (a.data.status !== 200){
                console.log(a.data)
                this.handleLogOutput("Invalid Credentials!")
                return
            }
            window.localStorage.setItem("token", a.data.token)
            window.location.href = '/'
        }
        catch(error){
            this.handleLogOutput("Database Unreachable!")
            console.log("database unreachable")
        }

    }
    
    /**
     * Render function.
     * @returns {html} The login form where the user must login in. Has 3 input boxes, 1 for username, 1 for password and another which is labeled as input even thought its a button.
     * This "button" can have its text changed so consider changing it to use button instead?
     */
    render() {
        return(
            <div>
                <div id="caixa-login" className="caixa-form">
                <h1 id="login-title" className="title-form">
                    <b>Login</b>
                </h1>
                <form id="form-login" className="formulario" onSubmit={this.handleSubmit} noValidate>
                    {/*<div id="form-login" className="formulario">*/}
                        <div className="texto-info">
                            <p className='paragraph' ref = {this.logRef}>
                                {this.state.log}
                            </p>
                        </div>
                        <InputField label="Username" value="username" onChange={this.handleUsernameInput}/>
                        <InputField label="Password" value="password" onChange={this.handlePasswordInput}/>
                        <button type='button' className="sign-up" onClick={()=>{window.location.href = "/register"}}>Sign Up</button>
                        <button
                            className='button-default'
                            type="submit"  // You can omit this attribute or set it to "button" (default behavior)
                            id="login"
                            onClick={() => this.submit(this.state)}
                        >
                        Submit
                        </button>
                    {/*</div>*/}
                </form>
                </div>
            </div>
        );
    }
}

class RegisterForm extends Component {
        /**
     * Constructor for RegisterForm Component.
     * ATTENTION!! IF CODE DOESNT WORK PLEASE REMOVE STATE FROM THE CONSTRUCTOR AND PUT IT OUTSIDE OF IT!!
     * @param {state} state Variable which holds information which may change during lifetime of this component
     * @param {String} email The email of the user
     * @param {String} username The username of the user
     * @param {String} password The password of the user
     * @param {String} log Message warning the user where to register if he has an account
     * @param {React.ref} logRef
     */
        constructor(){
            super()
            this.state = {
                email: '',
                username: '',
                password: '',
                log: ''
            }
            this.logRef = React.createRef()
        }
    
    
    handleUsernameInput = event => {
        this.setState({username: event.target.value})
    }
    /**
     * Set the value of event as the password
     * @param {String} event 
     */
    handlePasswordInput = event => {
        this.setState({password: event.target.value})
    }

    /**
     * Updates the email state with the value of the input field.
     * @param {Event} event - The input event triggered by the user.
     */
    handleEmailInput = event => {
        this.setState({email: event.target.value})
    }

    /**
     * Sets the value of str as the log message with the color Red.
     * @param {String} str 
     */
    handleLogOutput = (str) => {
        this.logRef.current.style.color = "red"
        this.setState({log: str.trim()})
    }

    /**
     * Handles form submission.
     * @param {Event} event - The form submission event.
     */
    handleSubmit = event => {
        event.preventDefault(); // Prevents the default form submission behavior
        this.submit(this.state); // Calls the submit method with the current state
    };

    /**
     * Handles form submission.
     * @param {Event} event - The form submission event.
     */
    handleSubmit = event => {
        event.preventDefault(); // Prevents the default form submission behavior
        this.submit(this.state); // Calls the submit method with the current state
    };

    /**
     * Validates the string name received as parameter by matching it with illegal characters and size
     * @param {String} name username of the user
     * @returns {String} A string of lenght 0 if the username is valid else one of the other options
     */
    useUsernameValidation = (name) => {
        let validRegEx = "^[a-zA-Z0-9_-]+$"

        if (name.length < 6 || name.length > 18) {
            return "Username must be between 6 and 18 characters"
        }

        console.log(name.match(validRegEx))
        if (!name.match(validRegEx)) {
            return "Username must contain only alphanumerical characters, '-' and '_'"
        }
        return ""
    }
    
    /**
     * Validades the string pass received as parameter by matching it with illegal characters and size
     * @param {String} pass password of the user
     * @returns {String} A string of lenght 0 if the username is valid else one of the other options
     */
    usePasswordValidation = (pass) => {
        let validRegEx = "^[a-zA-Z0-9_\\-#$%&@]+$"

        if (pass.length < 8 || pass.length > 18) {
            return "Password must be between 8 and 18 characters"
        }

        console.log(pass.match(validRegEx))
        if (!pass.match(validRegEx)) {
            return "Password must contain only alphanumerical characters, '-', '_', '#', '$', '%', '&' and '@'"
        }
        return ""
    }

    /**
     * Validates the email format.
     * @param {string} email - The email to be validated.
     * @returns {string} - Returns an empty string if the email is valid, otherwise returns an error message.
     */
    useEmailValidation = (email) => {
        let validRegEx = "^[a-z0-9._]+@[a-z0-9]+([.][a-z0-9]+)+$"

        email = email.toLowerCase()
        console.log(email.match(validRegEx))

        if (email === "") {
            return "Email field is empty"
        }
        if (!email.match(validRegEx)) {
            return "Invalid Email address format"
        }

        return ""
    }

    /**
     * Will run the validation functions and post in the DataBase the data of the user then redirect them to the main page.
     * @param {state} state State variable defined on the constructor
     * @returns if the string received by the validation functions is different than "" or the database is unreachable
     */
    async submit(state){

        const isEmailValid = this.useEmailValidation(this.state.email);
        const isUsernameValid = this.useUsernameValidation(this.state.username);
        const isPasswordValid = this.usePasswordValidation(this.state.password);

        if (isEmailValid !== "" || isPasswordValid !== "" || isUsernameValid !== "") {
            this.handleLogOutput(`${isEmailValid};${isUsernameValid};${isPasswordValid}`)
            return
        }

        let a = await DataFetchPost('api/register/', {
            email: this.state.email,
            username: this.state.username,
            password: this.state.password,
        })
        console.log(a)

        if (a.data.status !== 200){
            console.log(a.data)
            if (a.data.status === 500) this.handleLogOutput("Username already exists!");
            return
        }
        
        window.localStorage.setItem("token", a.data.token)
        window.location.href = '/'
    }

    /**
     * Render function
     * @returns {html} The register form where the user must register in. Has 3 input boxes, 1 for username, 1 for password and another which is labeled as input even thought its a button.
     * This "button" can have its text changed so consider changing it to use button instead? 
     */
    render() {
        return(
            <div>
                <div id="caixa-register" className="caixa-form">
                <h1 id="register-title" className="title-form">
                    <b>Register</b>
                </h1>
                <form id="form-register" className="formulario" onSubmit={this.handleSubmit} noValidate >
                    {/*<div id="form-register" className="formulario">*/}
                        <p ref = {this.logRef} className="texto-info">
                            {
                            this.state.log.split(';').map((item, i) => {
                                return <p  key={i}>{item}</p>
                            })
                            }
                        </p>
                        <InputField label="Email" value="email" onChange={this.handleEmailInput}/>
                        <InputField label="Username" value="username" onChange={this.handleUsernameInput}/>
                        <InputField label="Password" value="password" onChange={this.handlePasswordInput}/>
                        <button type='button' className="sign-up" onClick={()=>{window.location.href = "/login"}}>Sign In</button>
                        <button
                            className='button-default'
                            type="submit"  // You can omit this attribute or set it to "button" (default behavior)
                            id="login"
                            onClick={() => this.submit(this.state)}
                        >
                        Submit
                        </button>
                    {/*</div>*/}
                </form>
                </div>
            </div>
        );
    }
}

/**
 * Login component.
 * Renders all the components in this page.
 * @returns {html} the main contents of the site
 */
const Login = (props) => {
    return (
        <>  
            <Header/>
            <main>
                {props.type === 'login' ? <LoginForm/> : <RegisterForm/>}
            </main>
        </>
    );
}

export default Login;
