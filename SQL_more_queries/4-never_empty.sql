-- create a table id_not_null
-- id has a default value of 1
-- so id can never be null

CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(255));
