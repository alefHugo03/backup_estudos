CREATE DATABASE IF NOT EXISTS teste_trigger;
USE teste_trigger;

DELIMITER //

CREATE PROCEDURE sp_alterar_valor (
    IN valor INT,
    IN nome VARCHAR(50)
)
BEGIN
    UPDATE produtos
    SET preco = valor
    WHERE nome_produto = nome;
END //
DELIMITER ;