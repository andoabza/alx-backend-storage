-- create trigger that reset valid_email to false when email is updated
drop Trigger if exists reset_valid_email;
DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
   IF NEW.email <> OLD.email THEN
      SET NEW.valid_email = 0;
   END IF;
END;
DELIMITER ;