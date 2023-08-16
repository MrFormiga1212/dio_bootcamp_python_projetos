CREATE DATABASE OficinaDB;
USE OficinaDB;
-- Criação da tabela Cliente
CREATE TABLE Cliente (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Telefone VARCHAR(20),
    Endereco VARCHAR(200)
);

-- Criação da tabela Veiculo
CREATE TABLE Veiculo (
    Placa VARCHAR(10) PRIMARY KEY,
    Modelo VARCHAR(50),
    Ano INT,
    ClienteID INT,
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ID)
);

-- Criação da tabela Servico
CREATE TABLE Servico (
    ID INT PRIMARY KEY,
    Descricao VARCHAR(200),
    Preco DECIMAL(10, 2)
);

-- Criação da tabela OrdemDeServico
CREATE TABLE OrdemDeServico (
    ID INT PRIMARY KEY,
    Data DATE,
    VeiculoPlaca VARCHAR(10),
    ClienteID INT,
    FOREIGN KEY (VeiculoPlaca) REFERENCES Veiculo(Placa),
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ID)
);

-- Criação da tabela de associação ServicoOrdem
CREATE TABLE ServicoOrdem (
    OrdemID INT,
    ServicoID INT,
    PRIMARY KEY (OrdemID, ServicoID),
    FOREIGN KEY (OrdemID) REFERENCES OrdemDeServico(ID),
    FOREIGN KEY (ServicoID) REFERENCES Servico(ID)
);
