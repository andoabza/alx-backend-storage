-- create divider FUNCTION
DELIMITER $$
CREATE FUNCTION safeDiv (a INT, b INT)
    RETURNS INT
    DETERMINISTIC
    BEGIN
        DECLARE result INT;
            SET result = a DIV b;
        RETURN result;
    END$$
DELIMITER ;
```