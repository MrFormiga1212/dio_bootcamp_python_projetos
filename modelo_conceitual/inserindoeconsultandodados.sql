-- Inserindo dados na tabela Cliente
INSERT INTO Cliente (ID, Nome, Telefone, Endereco)
VALUES
    (1, 'João Silva', '(11) 1234-5678', 'Rua A, 123'),
    (2, 'Maria Santos', '(22) 9876-5432', 'Avenida B, 456');

-- Inserindo dados na tabela Veiculo
INSERT INTO Veiculo (Placa, Modelo, Ano, ClienteID)
VALUES
    ('ABC123', 'Sedan', 2020, 1),
    ('XYZ789', 'SUV', 2018, 2);

-- Inserindo dados na tabela Servico
INSERT INTO Servico (ID, Descricao, Preco)
VALUES
    (1, 'Troca de óleo', 100.00),
    (2, 'Balanceamento de rodas', 50.00);

-- Inserindo dados na tabela OrdemDeServico
INSERT INTO OrdemDeServico (ID, Data, VeiculoPlaca, ClienteID)
VALUES
    (1, '2023-08-16', 'ABC123', 1),
    (2, '2023-08-15', 'XYZ789', 2);

-- Inserindo dados na tabela ServicoOrdem (Associação)
INSERT INTO ServicoOrdem (OrdemID, ServicoID)
VALUES
    (1, 1),
    (1, 2),
    (2, 1);

-- Recupera todos os clientes
SELECT * FROM Cliente;

-- Recupera todos os veículos
SELECT * FROM Veiculo;

-- Recupera todos os serviços
SELECT * FROM Servico;

-- Recupera veículos de um determinado modelo
SELECT * FROM Veiculo WHERE Modelo = 'Sedan';

-- Recupera ordens de serviço de uma data específica
SELECT * FROM OrdemDeServico WHERE Data = '2023-08-16';

-- Recupera veículos de um determinado modelo
SELECT * FROM Veiculo WHERE Modelo = 'Sedan';

-- Recupera ordens de serviço de uma data específica
SELECT * FROM OrdemDeServico WHERE Data = '2023-08-16';

-- Recupera veículos de um determinado modelo
SELECT * FROM Veiculo WHERE Modelo = 'Sedan';

-- Recupera ordens de serviço de uma data específica
SELECT * FROM OrdemDeServico WHERE Data = '2023-08-16';

-- Recupera veículos de um determinado modelo
SELECT * FROM Veiculo WHERE Modelo = 'Sedan';

-- Recupera ordens de serviço de uma data específica
SELECT * FROM OrdemDeServico WHERE Data = '2023-08-16';

-- Recupera veículos de um determinado modelo
SELECT * FROM Veiculo WHERE Modelo = 'Sedan';

-- Recupera ordens de serviço de uma data específica
SELECT * FROM OrdemDeServico WHERE Data = '2023-08-16';
