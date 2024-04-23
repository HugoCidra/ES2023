import React, {Component} from 'react';
import './admin.css';
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import Profile from '../../IMAGES/profile_photo.png';
import Popup from 'react-popup';

var fileDownload = require('js-file-download');

/*
  - Função para realizar o download do arquivo.
    (Arquivo exportado no nome "filename.xml"? Deveria ter um nome mais autoexplicativo?)
*/

function FileB() {
    const handlePDFDownload = () => {
        DataFetchGet('api/REQ7/send_info/', { 
          responseType: 'blob',
        }).then(res => {
            let data = res.data
            if (data['status'] === 405){            //Verificação do estado da resposta da Base de Dados
                console.log(data['log'])
                return
            }else if (data['status'] === 500){
              Popup.alert(data['log']);
              setTimeout(() => {
                Popup.close();
              } , 7000);
              window.location.href="/login";
              return;
            }else if (data['status'] === 505){
              Popup.alert(data['log']);
              setTimeout(() => {
                Popup.close();
              } , 7000);
              return;
            }
            
            Popup.alert('Quizzes exported successfully!');
            setTimeout(() => {
              Popup.close();
            } , 7000);
            fileDownload(res.data['data'], 'filename.xml');
            console.log(res);
        })
        return
}
return (
    <div>
      <>
       <button onClick={() => handlePDFDownload()}>Export</button>
       </>
    </div>
    )
}

//Construtor da classe FileA

class FileA extends Component {

  constructor(props) {
    super(props);

    this.state = {
      file: null
    };

    this.sendFile = this.sendFile.bind(this);

    

    // Cria uma referência para o input de arquivo
  this.fileInputRef = React.createRef();
  }

  // Novo método para abrir o diálogo de seleção de arquivos
  openFileSelector = () => {
    this.fileInputRef.current.value = ''; // Limpa o input para permitir que  o mesmo arquivo seja selecionado se necessário
    this.fileInputRef.current.click(); // Abre o diálogo de seleção de arquivos
  }

  handleInputChange = async (event) => {
    event.preventDefault();
    const file = event.target.files[0];
    if (file) {
      await this.setState({ file: file });
      this.sendFile(); // Enviar o arquivo logo depois de ser selecionado
    }
  };

  //Função para enviar um arquivo
  async sendFile(){
    
    

    if (!this.state.file) {
      
      
    return;
      
    }

    let data = new FormData();
    data.append("file", this.state.file); // Adiciona o arquivo ao formulário de dados

    let a = await DataFetchPost('api/REQ7/load_info/', data) //Faz um POST para carregar as informações
    
    //Verifica o status da resposta de aquisição
    if (a.data['status'] === 505){
          Popup.alert(a.data['log']);
          setTimeout(() => {
            Popup.close();
          } , 7000);
          return
    }else if (a.data['status'] === 500){
      Popup.alert(a.data['log']);
      setTimeout(() => {
        Popup.close();
      } , 7000); 
      window.location.href="/login"
      return
    }
    //Alerta indicando que o Quizz foi lido com sucesso
    Popup.alert('Quizzes read successfully!');
    setTimeout(() => {
      Popup.close();
    } , 7000);
    console.log(a);//log da resposta do console (Por que "a"?)


    this.setState({ file: null });


  }

  render() {
    return (
      <>
        <input
          type="file"
          name="file" 
          onChange={this.handleInputChange}
          style={{ display: 'none' }}
          ref={this.fileInputRef}
        />
        <button onClick={this.openFileSelector}>Import</button> {/* Botão chama a função para abrir o seletor de arquivo */}
      </>
    );
  }
}

class Nome extends Component {
  constructor() {
    super();
    this.state = {
      username: ""
    };
  }
  handleProfileClick = () => {
    window.location.href = '/profile';
  };

  async componentDidMount() {
    // Fazer a solicitação à base de dados para obter o username
    try {
      let response = await DataFetchGet('api/REQ8/get_username/', null);
         
      console.log(response);
         
      this.setState({ username: response['data'].username });
      this.setState({ status: response['data'].status });
          
    } catch (error) {
        console.log("error", error);
    }
  }

  render() {
    return (
      <p className="nome" onClick={this.handleProfileClick}>
        {this.state.username}
      </p>
    );
  }
}

class ProfileGet extends Component{
  handleProfileClick = () => {
    window.location.href = '/profile';
  };
  
  render() {
    return (
      <div className="container" onClick={this.handleProfileClick}>
        <img src={Profile} alt="Profile" id="ProfileButton" height="45" width="45" />
      </div>
    );
  }
}

const Admin = () => {
  return (
    <>
      <div className="ports-container">
        <div className="container">
        <ProfileGet/>
        <Nome/>
        </div>
        <div className="separator"></div>
        <FileA />
        <FileB />
        <button><a href="/login">Log Out</a></button>
      </div>
    </>
  );
}
export default Admin;


