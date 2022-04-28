# ATIVA-SYSTEM

A priore a ideia é ler os dados do cliente e tratalos de forma que possamos criar dois arquivos para importação, txt e xlsx.

## Bibiliotecas  Urilizadas:

- **Sqlite3**
- **Openpyxl**
- **Shutil**
- **Os**
- **Datatime**
---
## Como o Robo Foi Feito?:

1. O robo lé uma planilha a qual armazena em um alista as informações necessarias para se realizar um depara.
2. O depara foi criado apartir de um *Database* o qual asmazena os parametros desenvolvidos pelo contabil para assosciar as informaçôes da planilha.
3. Apos o depara de inforamçôes o sistema cria uma planilha e escreve as inforamçôes nela salvando a como teste2.xlsx
4. em seguida gera um arquivo txt para ser importado para a dominio
5. Ao fim do processo ele armazena o txt e o xlsx na pasta de donwloads do usuario.
---
## Descrição de Pastas e Arquivos:

* ### [database ](https://github.com/Alldax-Contabilidade/ATIVA-SYSTEM/tree/main/database).
  * [acessadb.py](https://github.com/Alldax-Contabilidade/ATIVA-SYSTEM/blob/main/database/acessadb.py)
  > Aqui é aonde acesso o banco de dados com os deparas e busco a sinforamções
  * DBatsy.db
  > Este é o arquivo copia do banco de dados, camo queria estudar a estrutura do banco de dados.
  
  **Caso queira acesar o arquivo original do banco de dados o caminho é: T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\Ativa_system**
* ### [planilhas](https://github.com/Alldax-Contabilidade/ATIVA-SYSTEM/tree/main/planilhas).
  *[leitura.py](https://github.com/Alldax-Contabilidade/ATIVA-SYSTEM/blob/main/planilhas/leitura.py)
  > Neste arquivo ele le a planilha selecionada pelo usuario e coleta as informaçoes necessarias para o depara e importação.
  
  *[escrevendo.py](https://github.com/Alldax-Contabilidade/ATIVA-SYSTEM/blob/main/planilhas/escrevendo.py)
  > Apos ler a planilha e realizar o depara, aqui ele gera o arquivo xlsx com as informações necessarias par aa importação.
  * teste.xlsx
  > Essa planilha é o arquivo teste utilizado para rodar o codigo como planilha do usuario.
  * teste2.xlsx
  > Esta é a planilha final utilizada para gerar o arquivo txt.