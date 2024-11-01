--ATIVIDADE: Crie uma nova tabela chamada 'professores', com a mesma quantidade de características de 'alunos',
--fazendo ao menos duas injeções de dados e uma consulta.

CREATE TABLE professores (
    matricula INTEGER PRIMARY KEY,
    nome_professor TEXT NOT NULL,
    materia TEXT NOT NULL
);

-- injeção de dados-teste
INSERT INTO professores VALUES (1, 'Marina', 'Matemática');
INSERT INTO professores VALUES (2, 'Joana', 'Português');

-- consultando as injeções realizadas
SELECT * FROM professores WHERE matricula=2;
