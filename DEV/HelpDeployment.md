#   Acesso à VM do DEI e Deployment


### Antes de aceder à VM

-   Será necessária a instalação do VPN do DEI que pode ser feita segundo este tutorial do helpdesk https://helpdesk.dei.uc.pt/configuration-instructions/vpn-access/ . 
-   Para ter acesso ao tutorial é necessário o login com o username do email do DEI (o endereço sem @student.dei.uc.pt) e a password deste email.

---

### Importante

-   Para conseguir correr a aplicação na VM tiveram de ser feitas alterações relacionados com os portos de acesso e com os endereços de IP. Para facilitar a compatibilidade entre ambientes foram utilizados ficheiros com variáveis de ambiente:

    -   Um dos ficheiros foi criado na pasta DEV com as variáveis necessárias para alterar valores nos ficheiros docker-compose.yml e settings.py 

        ############### \
        #Documento .env criado para resolver compatibilidades de deploy no servidor do DEI. \
        #Para correr no Server do DEI descomentar o bloco "SERVER". \
        #Para correr na máquina local descomentar o bloco "LOCAL". \
        #Este ficheiro deve estar na pasta DEV \
        ###############

        #LOCAL \
        DEBUG=True \
        HOST_IP=127.0.0.1 \
        PORT=8000 \
        ALLOWED_HOSTS=127.0.0.1,localhost \
        CORS_ORIGIN_WHITELIST=http://127.0.0.1:3000,http:// localhost:3000 
    

    ---
    -   Dependendo de como ficou instalado o npm em cada máquina pode ser necessário fazer npm install dotenv dentro da pasta frontend para os ficheiros DataFetchGet, DataFetchPut e DataFetchPost conseguirem ir buscar os valores das variáveis de ambiente.

    -   O outro ficheiro foi criado na pasta frontend com as variáveis necessárias para alterar os valores das variáveis nos ficheiros DataFetchGet.js, DataFetchPut.js e DataFetchPost.js
      
        (IMPORTANTE: Dependendo de como ficou instalado o npm em cada máquina pode ser necessário fazer npm install dotenv dentro da pasta frontend para os ficheiros conseguirem ir buscar os valores das variáveis de ambiente).

        ############### \
        #Documento .env criado para resolver compatibilidades de deploy no servidor do DEI. 
        #Para correr no Server do DEI descomentar o bloco "SERVER".
        #Para correr na máquina local descomentar o bloco "LOCAL".
        #Este ficheiro deve estar na pasta DEV/frontend \
        ############### \
        #LOCAL\
        REACT_APP_API_URL=http://localhost:8000/ \
        #SERVER \
        #REACT_APP_API_URL=http://10.17.0.189:8080/

-   Dentro dos ficheiros .env estão comentadas estas instruções caso seja necessário consultá-las outra vez.

---

### Acesso 
-   Abrir a cmd;
-   Fazer o login com ssh admin@10.17.0.189 (password: espl1admin);
-   Navegar para a diretoria Documents/ES/pl1/DEV ;
-   Para correr a aplicação usar o comando sudo docker-compose up;
-   Para ver a aplicação a correr visitar a página web http://10.17.0.189:3000/ ;
-   Para parar a execução utilizar CTRL+C e no final fazer sudo docker-compose down ;

