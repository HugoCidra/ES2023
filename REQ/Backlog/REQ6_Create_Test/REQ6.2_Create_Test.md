# REQ6.2 - Create new Test

- **PRIMARY ACTOR:** Creator

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Creators, Solvers

- **PRECONDITIONS:**
1. Creator is logged on
2. At least 20 quizzes available 

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Creator can create a new test

- **MAIN SUCESS SCENARIO:**
1. Creator enters '/create-test' page
2. System shows page with Title box , all 12 tags, Submit and Cancel options
3. Creator selects 2 TAGS
4. Creator clicks 'SUBMIT'
5. System feedback with all TAGS and nr of the Test
6. System redirects to '/'

- **EXTENSIONS/ALTERNATIVE PATHS:**

2. (a) Precondition 'At least 20 quizzes available ' fails -> back to '/' page

4. (a) Creator clicks 'SUBMIT' without 2 TAGS selected
5. (b) System feedback: 'Please select 2 TAGS'

---

# Guidelines & Restrictions

- Select 2 TAGS from 12 AVAILABLE: 
1. PM  (Gestão de projecto)
2. REQ (requisitos)
3. A&D (Arquitectura e design)
4. IMP (Implementação)
5. TST (testes e qualidade de produto)
6. V&V (Verification and Validation)
7. DEP (deployment)
8. CI  (Continuous practices)
9. PRC (boas-práticas e qualidade de PRocessos)
10. PPL (Peopleware)
11. CCM (Configuration and Change Management)
12. RSK (Risk management)
NOTA: um quizz pode ter MAIS que uma tag, mas tem de ter no mínimo uma tag.

- Guidelines from our Client:

1. Um teste consiste num conjunto de quizzes (N = 20).
2. Cada quizz só pode estar incluído, no máximo, em dois testes.
3. A criação de testes implica seleccionar as tags dos temas que se deseja incluir no teste. Por exemplo, seleccionando apenas as tags "PM e REQ" a vossa aplicação vai à lista de quizzes disponíveis e escolhe aleatoriamente 10 (N/2) quizzes que tenham a categoria PM e 10 (N/2. quizzes que tenham a categoria REQ (usem aritmética de inteiros).
4. Se não houver quizzes disponíveis de uma dada categoria, o número de quizzes de um tipo 'em falta' passa para as restantes categorias, por qualquer ordem.
5. Se não houver nenhum quizz em nenhuma das categorias seleccionadas, o teste não é criado e o criador notificado disso. (REQ6.4 apenas)
6. Quando um teste acaba de ser criado, o criador de testes tem de poder saber qual a distribuição efectiva de quizzes por tags (e.g. 10xREQ, 5xPM, 3xIMP, 2xTST). vii. Aliás, esse 'perfil' de tags tem de fazer parte da descrição do teste para os 'resolvedores' poderem escolher os testes que querem realizar. (REQ6.3 apenas)
7. Um teste tem de ter um 'título' (e.g. "Teste Geral", "Anda testar se és um dev", "Teste para frontenders", "Teste do Pixinguinha",...)
8. O criador de testes não vê as questões que foram incluídas, apenas vê o perfil de tags (e o título que ele próprio deu).