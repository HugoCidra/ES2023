import '../index.css';
import '../Review_Quiz/button.css'
import './style_tags.css'
import React from 'react'
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';
import DataFetchGet from "../../DataFetchFunctions/DataFetchGet";
import NavBar from '.././NavBar/NavBar';
import Popup from 'react-popup';

/*  
  Class for the test creation page
*/

class CreateTest extends React.Component {
  
 /**
   * Constructor for the CreateTest class.
   * @param {object} props - The properties passed to this component.
   */

  constructor(props) {
    super(props);
    this.state = {
      title: '', //Título do teste
      tags: [], //Tags selecionadas
      get: {} //Dados obtidos pelo GET da base de dados
    };

    this.handleTitleChange = this.handleTitleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

 /**
   * Function called after the component is mounted.
   * Performs a GET request to fetch available tags and updates the state.
   */

  async componentDidMount() {
    try {
      const response = await DataFetchGet('api/REQ6/tags/', null);
      console.log(response);
      this.setState({
        title: this.state.title,
        tags: this.state.tags,
        get: response
      });
    } catch (error) {
      console.log("error", error);
    }
  }
  
  /**
   * Function used to submit the test creation.
   * @param {Event} event - The event object when the form is submitted.
   */

  async handleSubmit(event) {
    if (this.state.tags.length !== 2) {
      //Alerta que não foi selecionado 2 tags
      Popup.alert("You must select 2 tags.");
      setTimeout(() => {
        Popup.close();
      } , 7000);
    } else if (this.state.title.length < 10) {
      //Alerta que o título está com menos de 10 caracteres
      Popup.alert("The test must have a title with at least 10 characters.");
      setTimeout(() => {
        Popup.close();
      } , 7000);
    } else {
      console.log(this.state);

      let data_post_create_test = JSON.stringify({
        title: this.state.title,
        tags: this.state.tags
      });
      console.log(data_post_create_test);

      try {
        let result=await DataFetchPost('api/REQ6/test/', data_post_create_test); //Faz um POST para criar o teste
        console.log(result);
        if (result.data.status === 400) {
          //Alerta de erro ao criar o teste
          Popup.alert("Cannot create test; " + result.data.errors);
          setTimeout(() => {
            Popup.close();
          } , 7000);
        }
        else {
          let tagtext = "";
          console.log(result.data.count);
          /*
          * {
          * 'PM': 5
          * 'REQ': 5
          * }
          *
          * */
          for (const key in result.data.count) {
            tagtext += result.data.count[key] + ' X ' + key + ';\n'; //Formata a contagem de tags
          }
          tagtext = tagtext.slice(0, tagtext.length - 2);
          //Alerta de sucesso da criação do teste
          Popup.alert('Test created successfully! \n' + tagtext);
          setTimeout(() => {
            Popup.close();
            window.location.href = '/';
          } , 7000);
        }
        setTimeout(() => {window.location.href = '/'}, 1000);
      } catch (error) {
        console.error(error.response.data);     // NOTE - use "error.response.data` (not "error")  
      }
    }
    
    event.preventDefault();
  }

  /**
   * Function to change the test title.
   * @param {Event} event - The event object when the title input changes.
   */

  handleTitleChange(event) {
    this.setState({
      title: event.target.value,
      tags: this.state.tags,
      get: this.state.get
    });
    event.preventDefault();
  }

  /**
   * Function to handle tag button click.
   * @param {string} tagName - The name of the tag that was clicked.
   */

  handleTagButtonClick (tagName) {
    let changeButton = false;
    const existsTag = (element) => element === tagName;
    let tagIndex = this.state.tags.findIndex(existsTag);
    if (tagIndex === -1) {
      if (this.state.tags.length < 2) {
        this.state.tags.push(tagName); //Adiciona a tag se não existe
        changeButton = true;
      }
    } else {
      this.state.tags.splice(tagIndex, 1); //Remove uma tag já existente~
      changeButton = true;
    }
    console.log(this.state);
    return changeButton;
  }

  /**
   * Render the CreateTest component on the screen.
   * @returns {JSX.Element} - Returns the JSX element representing the CreateTest component.
   */

  render() {
       if(this.state.get.data === undefined) {
         return <>
         <NavBar/>
         <div className='CreateTest_instruction'>
          <div className="pergunta" >Create Test is not available</div>
         </div>
         </>
    } else return <>

        <div className='CreateTest_instruction'>
        <NavBar />
        <div className='containerExt'>
        <div className='title-container' >
          <span className='title'>TITLE</span>
          <span className='descricao'>(Minimum 10 characters)</span>
        </div>
        <input
          type='text'
          id="test-title-box"
          value={this.state.title}
          onChange={this.handleTitleChange}
          placeholder="Enter a title "
        />

        <div className='title-container' >
          <span className='title'>TAGS</span>
          <span className='descricao'>(choose 2)</span>
        </div>
        
        <div className="container-tags">
            
            

          {this.state.get.data.tags.map((name, key) => {
            return (
                <ButtonTag  name={name} onClick={() => this.handleTagButtonClick(name)}/>
            );
          })}

        </div>
      
      <button className="button-default submit_button" onClick={this.handleSubmit}>SUBMIT</button>
      <button className="cancel_button" onClick={() => { window.location.href = '/'; }}>CANCEL</button>
     
      </div>

      </div>
    </>
  

  }
}

  /**
   * Component to represent a tag button.
   * @param {Object} props - The properties passed to this component.
   */

const ButtonTag = ({ name, onClick }) => {
    function handleClick(e) {
      if (!onClick()) { 
        Popup.alert("You must select 2 tags.");
        setTimeout(() => {
          Popup.close();
        } , 7000);
        return; 
      }

      if(e.target.className === "tag_button") e.target.className="tag_button_click";
      else e.target.className="tag_button";
    };
  
  return < button onClick={e=>{handleClick(e)}} className="tag_button">{name} </button>;
}



export default CreateTest;





