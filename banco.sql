-- ATENÇÃO!!!! ESTE ARQUIVO  É APENAS UM EXEMPLO DA CRIAÇÃO DAS TABELAS
-- NA APLICAÇÃO app.py, É UTILIZADO O MONGODB, QUE NÃO NECESSITA DE CRIAÇÃO DE TABELAS
-- ARQUIVO CRIADO APENAS PARA CUMPRIR O REQUISITOSa


CREATE DATABASE compradb;

USE compradb;


CREATE TABLE comprascol (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Chave primária com auto-incremento
    nome VARCHAR(255) NOT NULL,        -- Nome do produto
    fornecedor VARCHAR(255) NOT NULL, -- Nome do fornecedor
    endereco_fornecedor VARCHAR(255), -- Endereço do fornecedor
    quantidade INT NOT NULL,          -- Quantidade do produto
    endereco VARCHAR(255),            -- Endereço do produto
    preco_unitario DECIMAL(10, 2)     -- Preço unitário do produto
);

-- Inserção de registros fictícios
INSERT INTO comprascol (nome, fornecedor, endereco_fornecedor, quantidade, endereco, preco_unitario)
VALUES
('Produto A', 'Fornecedor X', 'Rua 1, Cidade Y', 10, 'Rua 2, Cidade Z', 15.50),
('Produto B', 'Fornecedor Y', 'Rua 3, Cidade W', 20, 'Rua 4, Cidade V', 25.00),
('Produto C', 'Fornecedor Z', 'Rua 5, Cidade U', 15, 'Rua 6, Cidade T', 30.00),
('Produto D', 'Fornecedor W', 'Rua 7, Cidade S', 5, 'Rua 8, Cidade R', 50.00);