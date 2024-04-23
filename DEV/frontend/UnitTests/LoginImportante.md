# Importante

Antes de serem realizados os testes logValue e submit para o ficheiro Login.js devem ser feitas as seguintes alterações no código desse ficheiro, tendo como ponto de referência o ficheiro Login.js deste branch.

1. Na linha 137 foi adicionado data-testid="username-input"
2. Na linha 139 foi adicionado data-testid="password-input"

3. Na linha 307 foi adicionado data-testid="username-input2"
4. Na linha 319 foi adicionado data-testid="password-input2"

**Não foi removida qualquer linha do código original apenas foram adicionadas estas**

O data-testid não altera funcionalidades apenas serve para a realização dos testes. Estas labels permitem a realização correta dos testes, já que anteriormente os testes não corriam devido à semelhança entre as tags utilizadas no login e no registo, dando o erro "Found multiple elements with the id " ou "Found multiple elements with the same text".
