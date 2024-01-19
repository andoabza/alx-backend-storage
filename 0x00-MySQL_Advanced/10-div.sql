-- create divider FUNCTION
DELIMITER $$
CREATE FUNCTION safeDiv (a INT, b INT)
    RETURNS INT
    DETERMINISTIC
    BEGIN
        IF b = 0 THEN
            RETURN 0;
        END IF;
        RETURN a / b;
    END$$
DELIMITER ;