create schema pesquisa_site;

use pesquisa_site;

-- Tabela Cliente
CREATE TABLE Cliente (
    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefone VARCHAR(14)
);

-- Tabela  Pesquisa
CREATE TABLE Pesquisa (
    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    cliente_id INTEGER REFERENCES Cliente(id),
    nome_estado VARCHAR(255) NOT NULL,
    nome_cidade VARCHAR(255) NOT NULL,
    populacao INTEGER NOT NULL,
    eleitorado INTEGER NOT NULL,
    margem_erro INTEGER NOT NULL,
    confianca INTEGER NOT NULL,
    tipo_pesquisa VARCHAR(255) NOT NULL,
    qnt_perg INTEGER NOT NULL,
    qnt_urbanas INTEGER NOT NULL,
    qnt_rurais INTEGER NOT NULL,
);

-- Tabela Orçamento
CREATE TABLE Orcamento (
    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    pesquisa_id INTEGER NOT NULL,
    ambpg FLOAT NOT NULL,
    ambeg FLOAT NOT NULL,
    ambps FLOAT NOT NULL,
    ambes FLOAT NOT NULL,
    vp_bps FLOAT NOT NULL,
    vp_bes FLOAT NOT NULL,
    FOREIGN KEY (pesquisa_id) REFERENCES Pesquisa(id)
);


