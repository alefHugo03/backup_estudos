CREATE DATABASE IF NOT EXISTS teste_trigger;
USE teste_trigger;

DELIMITER //

CREATE TRIGGER tg_data_edicao
AFTER UPDATE ON produtos
FOR EACH ROW
BEGIN
    SET NEW.data_edicao = NOW();

    INSERT INTO log_produtos(preco_anterior, preco_atualizado, data_editada)
    VALUES (OLD.preco, NEW.preco, NEW.data_edicao);

END //
DELIMITER ;