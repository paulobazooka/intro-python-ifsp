DROP DATABASE IF EXISTS funcionarios;
CREATE DATABASE funcionarios;
USE funcionarios;

DROP TABLE IF EXISTS empregado;
CREATE TABLE empregado(id INT auto_increment primary key,
					   nome VARCHAR(75) not null, 
					   salario float not null);