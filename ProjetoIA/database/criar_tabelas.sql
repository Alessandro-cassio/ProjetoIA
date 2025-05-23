-- Tabela de plataformas (Uber, iFood)
CREATE TABLE plataformas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- Tabela de entregas
CREATE TABLE entregas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    distancia_km FLOAT,
    tempo_estimado_min INT,
    preco_frete DECIMAL(10, 2),
    disponibilidade_motoristas INT,
    plataforma_id INT,
    melhor_opcao BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (plataforma_id) REFERENCES plataformas(id)
);

-- Tabela de logs de decisões da IA
CREATE TABLE logs_ia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entrega_id INT,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    plataforma_escolhida VARCHAR(50),
    acuracia_modelo FLOAT,
    FOREIGN KEY (entrega_id) REFERENCES entregas(id)
);

-- SQL caso a empresa ja tenha os registros dos clientes 

CREATE DATABASE IF NOT EXISTS entrega_inteligente;
USE entrega_inteligente;

CREATE TABLE Empresa (
    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cnpj VARCHAR(20),
    endereco VARCHAR(200)
);

CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200)
);

CREATE TABLE Cooperado (
    id_cooperado INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(14),
    telefone VARCHAR(20),
    veiculo VARCHAR(50)
);

CREATE TABLE Plataforma (
    id_plataforma INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    taxa_servico DECIMAL(5,2)
);

CREATE TABLE Corrida (
    id_corrida INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_cooperado INT,
    id_plataforma INT,
    data_hora DATETIME,
    distancia_km DECIMAL(5,2),
    tempo_estimado_min DECIMAL(5,2),
    preco_frete DECIMAL(6,2),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_cooperado) REFERENCES Cooperado(id_cooperado),
    FOREIGN KEY (id_plataforma) REFERENCES Plataforma(id_plataforma)
);

CREATE TABLE Motorista (
    id_motorista INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(14),
    status_disponivel BOOLEAN
);

CREATE TABLE Entrega (
    id_entrega INT AUTO_INCREMENT PRIMARY KEY,
    id_corrida INT,
    status_entrega VARCHAR(50),
    horario_saida DATETIME,
    horario_entrega DATETIME,
    FOREIGN KEY (id_corrida) REFERENCES Corrida(id_corrida)
);

CREATE TABLE Pagamento (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_corrida INT,
    forma_pagamento VARCHAR(50),
    valor_pago DECIMAL(6,2),
    data_pagamento DATE,
    FOREIGN KEY (id_corrida) REFERENCES Corrida(id_corrida)
);

CREATE TABLE Avaliacao (
    id_avaliacao INT AUTO_INCREMENT PRIMARY KEY,
    id_corrida INT,
    nota INT,
    comentario TEXT,
    FOREIGN KEY (id_corrida) REFERENCES Corrida(id_corrida)
);

CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    login VARCHAR(50),
    senha VARCHAR(100),
    tipo VARCHAR(20)
);

CREATE TABLE LogSistema (
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    acao VARCHAR(100),
    data_hora DATETIME,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE IA_Registro (
    id_ia INT AUTO_INCREMENT PRIMARY KEY,
    id_corrida INT,
    melhor_opcao VARCHAR(50),
    prob_uber DECIMAL(5,2),
    prob_ifood DECIMAL(5,2),
    FOREIGN KEY (id_corrida) REFERENCES Corrida(id_corrida)
);
