import React from 'react';
import Logo from '../../IMAGES/Logo.png';
import Menu from '../../IMAGES/Menu.png';
import './NavBar.css';
import '../index.css';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import MenuModal from '../Menu/MenuModal'; 
import Popup from 'react-popup';

class NavBar extends React.Component {
  
  /**
   * Constructor for NavBar Component
   * @param {state} state Variable which holds information which may change during lifetime of this component
   * @param {String} username username of the user
   */
  constructor() {
    super();
    this.state = {
      menu_state: false,
      username: "",
      isMenuOpen: false // novo estado para controlar a visibilidade do menu
    };

    // Vincula a nova função ao contexto do componente
    this.toggleMenu = this.toggleMenu.bind(this);
    this.solve_button_action = this.solve_button_action.bind(this); // Garantir que `this` funciona dentro da solve_button_action
  }

  /**
   * React function. Called when NavBar is called and after the constructor.
   * Im not sure what this does but it saves the elements of something in an array.
   * Once that is done, it fetchs the DataBase for the username of the user.
   * If sucessfull sets the username as that value. There is no mention of status inside of state, maybe an error?
   */
  async componentDidMount() {
    let list_a = document.getElementById("links_nav").getElementsByTagName("a")
    let list_li=document.getElementById("links_nav").getElementsByTagName("li")
    for(let i=0;i<list_a.length;i++){
      //choose test case
      if(list_a[i].href===""){
        const aux= window.location.href.split("/")
        if(aux[aux.length-1]==="choose-test"){
          list_li[i].className="active-click"
        }
      }

      if (list_a[i].href === window.location.href){
        list_li[i].className="active-click"
      }
    }
    try {
      let response = await DataFetchGet('api/REQ8/get_username/', null);
      console.log(response);
      this.setState({ username: response['data'].username});
      this.setState({ status: response['data'].status});  
    } catch (error) {
        console.log("error", error);
    }
  }

  /**
   * Fetchs the DataBase for information about the user, asking if the user is a solver.
   * If he is, the user is redirected to "/choose-test", else, an alert will pop up warning the user that he must be a solver.
   */
  async solve_button_action(){
    let payload = await DataFetchGet('api/REQ2/is_solver/', null);
    console.log(payload);
    if(payload.data.response === false){
      Popup.alert("Must be a Solver");
      setTimeout(() => {
          Popup.close();
        } , 7000);
    }
    else{
      window.location.href = "/choose-test"
    }
  }

  // A função para alternar a visibilidade do menu
  toggleMenu() {
    this.setState({menu_state: !this.state.menu_state})
    console.log('------------------->',this.state.menu_state)
    this.setState(prevState => ({
      isMenuOpen: !prevState.isMenuOpen
    }));
  }

     
  /**
   * A collection of links disguised as buttons that when clicked send the user to a different part of the site
   * @returns {html} 
   */
  render(){
    return<>
    <meta charSet="UTF-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Quirked Up Software</title>
    <link rel="stylesheet" type="text/css" href="../../CSS/NavBar/NavBar.css"/>
          
        <main>
            <header>
            <nav id="navbar">
                <div>
                    <a href="/"><img src={Logo} alt="Logo" id="logo_return_home"/></a>
                </div>
                <ul id="links_nav">
                    <li><a href="/create-quizz">Create Quiz</a></li>
                    <li><a href="/review-quizz">Review Quiz</a></li>
                    <li><a href="/create-test">Create Test</a></li>
                    <li><a onClick={this.solve_button_action}>Solve Test</a></li>
                </ul>

                <div id="menuButton" onClick={this.toggleMenu}>
                  <span className={`line line1 ${this.state.menu_state && "active"}`}></span>
                  <span className={`line line2 ${this.state.menu_state && "active"}`}></span>
                  <span className={`line line3 ${this.state.menu_state && "active"}`}></span>
                </div>
                
            </nav>
            </header>
            <MenuModal modal={this.state.isMenuOpen} toggleModal={this.toggleMenu} />
        </main>
        </>
      }
  
}
  
export default NavBar;