-- create divider FUNCTION
DELIMITER $$
CREATE FUNCTION safeDiv (a INT, b INT)
    RETURNS INT
    DETERMINISTIC
    BEGIN
        DECLARE result INT;
        IF b = 0 THEN
            SET result = 0;
        ELSE
            SET result = a / b;
        END IF;
        RETURN result;
    END$$
DELIMITER ;
```