--###AULA02 - 23/10/2024###

--https://www.mysql.com/downloads/


--INTEGRAÇÃO PANDAS + MYSQL

--(NO TERMINAL)
--pip install sqlalchemy pymysql

--(código no arquivo .py)

--ATIVIDADE (github):

--Crie mais duas tabelas (sugestão: 'cursos' e 'filiais') no mesmo banco de dados
--onde você criou 'alunos' e 'professores'. Façam mais características para essas tabelas (ao menos 5)
--e criem, pelo menos, 10 injeções de dados para as novas tabelas e 1 consulta para cada uma delas. 
--No final, peça (no VSCode) para que o Pandas leia cada tabela nova que foi criada.

CREATE TABLE cursos (
	codigo INTEGER PRIMARY KEY,
    nome_curso TEXT NOT NULL,
    nivel TEXT NOT NULL,
    turno TEXT NOT NULL
    );
INSERT INTO cursos VALUES (1, 'Excel', 'Intermediário');
INSERT INTO cursos VALUES (2, 'Word', 'Básico');

CREATE TABLE filiais (
	codigo INTEGER PRIMARY KEY,
    nome_loja TEXT NOT NULL,
    bairro TEXT NOT NULL
    );
    
INSERT INTO filiais VALUES (1, 'Magalu', 'Méier');
INSERT INTO filiais VALUES (2, 'Magalu', 'Centro');



--PESQUISA: quais são diferenças de um DATAFRAME (Pandas) para uma SERIE (NumPy)?
