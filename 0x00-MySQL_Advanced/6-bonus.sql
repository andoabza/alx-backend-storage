-- create stored procedure that adds a new correction for a student.

DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
   DECLARE v_project_id INT;

   SELECT id INTO v_project_id FROM projects WHERE name = project_name;

   IF v_project_id IS NULL THEN
       INSERT INTO projects (name) VALUES (project_name);
       SET v_project_id = LAST_INSERT_ID();
   END IF;

   INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, v_project_id, score);
END $$
DELIMITER ;

