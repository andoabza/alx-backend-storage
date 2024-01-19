-- create stored procedure that adds a new avarege.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = p_user_id;

    UPDATE users SET average_score = avg_score WHERE id = p_user_id;
END$$
DELIMITER ;
