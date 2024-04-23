# Documentação em falta nos ficheiros de teste

#### Conteúdos:
    Test1.1_Register_EmptyNameEmptyPass.py
    Test1.2_Register_Existent_User_New_Pass.py
    Test1.3_Register_No_Problems.py
    Test1.4_Login_EmptyNameEmptyPass.py
    Test1.5_Login_Good_Name_Bad_Pass.py

## REQ1 (Test1.1_Register_EmptyNameEmptyPass)
 - O código é objetivo mas carece de qualquer tipo de comentários ou documentação que realmente ajudem a explicar o que está a ser feito visto que quem não conhecer a ferramenta Selenium não tem, até aqui qualquer instrução ou explicação relativa à mesma, tornando por vezes confuso, ainda que se consiga entender a ideia principal.

## REQ1(Test1.2_Register_Existent_User_New_Pass)
 - Mais uma vez o código não é longo mas não possui comentários ou documentação. A função time.sleep(x) poderá ser substituída por uma que não envolve uma espera ativa, otimizando o processo.

## REQ1 (Test1.3_Register_No_Problems) 
 - De novo fica evidente que a falta de comentários e documentação tornam o código um pouco confuso, sobretudo para quem nunca o tinha visto e não está familiarizado com as ferramentas usadas. A função time.sleep(x) poderá ser substituída por uma que não envolve uma espera ativa, otimizando o processo.


## REQ1 (Test1.4_Login_EmptyNameEmptyPass)
 - A espera ativa através da função time.sleep(x) torna a repetir-se e neste script várias vezes, indo ao encontro dos problemas levantados anteriormente. Com a análise de vários scripts o utilizador vai-se familiarizando com as ferramentas usadas mas em nenhum momentos há comentários ou documentação que elucidem algo, tratando-se por isso, da dedução do utilizador.

## REQ1 (Test1.5_Login_Good_Name_Bad_Pass) 
 - Mais uma vez os mesmos problemas verificam-se: o uso da função time.sleep(x), a falta de documentação e qualquer tipo de comentário, por muito curto e objetivo que possa ser o código.

 - Em todos os requisitos nota-se também a repetição de um determinado número de linhas de código, nomeadamente as necessárias para efetuar o login, dito isto seria mais prático 
criar um ficheiro.py de forma a evitar esta repetição.


## REQ1 (Test1.6_Login_No_Problem)

#### Conteúdos:
    Test1.1_Register_EmptyNameEmptyPass.py
    Test1.2_Register_Existent_User_New_Pass.py
    Test1.3_Register_No_Problems.py
    Test1.4_Login_EmptyNameEmptyPass.py
    Test1.5_Login_Good_Name_Bad_Pass.py
    Test1.6_Login_No_Problem.py

 - Ficheiro com pouco código e com funções simples, mas que podem ser modificadas para ficarem mais objetivas. Carece de comentários-chave relativamente ao próprio código e às bibliotecas importadas que são desconhecidas pela maioria dos utilizadores. 
  
 - Necessário realizar outra abordagem para o time.sleep(), dado que esta função não é a mais adequada para realizar a espera de alguns elementos que estão a carregar.


## REQ2 (- 2.4) 

#### Conteúdos: 
    Test2.1_Create_Quiz_Button
    Test2.2_Review_Quiz_Button
    Test2.3_Solve_Test_Button
    Test2.4_Not_Solver_Solve_Test_Button
    Test2.5_Profile_Button 
    Test2.6_Admin_Button
    Test2.7_Logout_Button 
    Test2.8_Draft_Redirect_Id

- Estes ficheiros também não constam de documentação, o que torna complicado a sua interpretação. Há também necessidade de melhorar o tratamento das exceções e como mencionado anteriormente é necessário colocar comentários-chave para assim haver uma interpretação fácil por parte de todos os utilizadores.

-  Dado que os testes têm em comum uma função (“login”), poderia-se criar um ficheiro.py com essa função de forma a não torná-la repetitiva entre os vários testes.


## REQ2(Test2.5,Test2.6,Test2.7,Test2.8)
 - Nestes ficheiros há grande falta de comentários nas funções, cada função deveria ter um comentário que explicasse o que esta faz, quais os parâmetros de entrada e o que retorna, para além das funções também ajudaria adicionar comentários a explicar as partes mais complexas do código ou a lógica do uso do código de certa maneira. Também seria interessante acrescentar instruções de uso, isto é, como executar o script e quais os pré-requisitos necessários. Algo a comentar no início do código seria o objetivo do teste. Outro aspecto importante seria adicionar um comentário que explicasse o significado dos resultados dos testes e como os valores são usados para ditar esse mesmo resultado. É também importante explicar a importância de no fim os recursos como o (diver) serem fechados adequadamente.

## REQ3(Test3.1_button)
 - Neste ficheiro todos os aspetos referidos a cima são relevantes, sendo que a estrutura é semelhante mas sendo um código ligeiramente maior que os anteriores a necessidade de comentários a explicar as funções, o que estas fazem e os parâmetros de entrada e saída são ainda mais necessários. Para além disso, dentro da função “test_buttons” seria necessário explicar o propósito de cada teste de botão, como e porque é feito. Por outro lado, nos comentários já feitos é necessária uma grande melhoria, sendo necessário adicionar informações adicionais.

## REQ3 (3.2-4.2)

#### Conteúdos:
    Scripts
        Selenium_Tutorial.py
        Test3.1_buttons.py
        Test3.2_Errors1.py
        Test3.2_Errors2.py
        Test3.2_Errors3.py
        Test3.3_Submit.py
        Test4.2_reject.py
    HowToTest.py
    Selenium_Tutorial.py

- Nesta pasta temos um breve tutorial de Selenium ligeiramente confuso, nomeadamente na linha 31. É conveniente rever este documento após um estudo sobre esta ferramenta no âmbito de realizar os testes automatizados.

- Estão também presentes os ficheiros de teste ‘Test3.2_Errors1-3’ que carecem de uma descrição breve das funções ‘test_errors1-3’, sendo o seu nome bastante genérico o que não evidencia que tipo de erro está a ser testado. O problema mencionado no tutorial persiste nos ficheiros acima mencionados e nos dois restantes. Ao correr-los, é levantada uma exceção nas linhas com ‘driver = webdriver.Chrome(ChromeDriverManager().install())’.

- À semelhança dos ficheiros referidos, as funções principais test_submit e test_reject (do Test3.3_Submit.py e Test4.2_reject.py respectivamente) necessitam de uma descrição que permita entender o seu conteúdo sem precisar de uma análise profunda do código.

- Para além do que já foi mencionado, acredita-se que seria uma mais valia que os blocos try/except contivessem um comentário a explicar em que situações as exceções tratadas são levantadas.


## REQ4

#### Conteúdos:
    Test4.3_accept.py
    Test4.2_reject.py
    Test4.3_accept.py

- Não consta de nenhuma documentação sobre os testes criados nesta pasta e os ficheiros .py necessitam de comentários chave, como por exemplo uma breve introdução pelo menos nas funções principais (e.g. test_buttons),  para que o código seja assim de fácil entendimento por parte de todos.


## REQ5

#### Conteúdos:
    Test5.1_Buttons.py
    Test5.2_Submit.py
    TEST5_3_choose_test.py

- Test5.1_Buttons e TEST5_3_choose_test também não constam de nenhuma documentação e os ficheiros .py necessitam de comentários chave para que sejam de fácil entendimento por parte de todos.

- O ficheiro Teste5.2_Submit.py inclui 8 funções sendo que não se verificam comentários em docstring e existem apenas alguns comentários simples pelo código pouco claros. Sendo assim é necessário a criação de docstrings que deixem explícito o propósito e as características de cada função podendo ainda ser usado comentários simples para tornar certas zonas do código mais claras quanto ao seu funcionamento.


## REQ7

#### Conteúdo:
    good_type_import_test.xml
    scary_type_import_test.pdf
    Test7.1_Import_Wrong_Type.py
    Test7.2_Import_Right_Type.py
    Test7.3_Export.py

- Esta pasta inclui 1 xml, 1 pdf e 3 scripts de python sendo que não se verificam comentários em docstring e existem apenas alguns comentários simples pelo código pouco claros. Sendo assim necessário a criação de docstrings que deixem explícito o propósito e as características de cada função podendo ainda ser usado comentários simples para tornar certas zonas do código mais claras quanto ao seu funcionamento.
  
-  É necessário ainda um .md com uma descrição muito breve sobre o conteúdo presente na pasta.


## REQ8

#### Conteúdo:
    Test8.1_Username.py

- Esta pasta inclui 1 script de python sendo que não se verificam comentários em docstring nem comentários simples. Sendo assim necessário a criação de docstrings que deixem explícito o propósito e as características das funções presentes, podendo ainda ser usado comentários simples para tornar certas zonas do código mais claras quanto ao seu funcionamento.

-  É necessário ainda um .md com uma descrição muito breve sobre o conteúdo presente na pasta.
