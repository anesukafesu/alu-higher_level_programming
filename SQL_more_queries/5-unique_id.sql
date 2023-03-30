-- create a table unique_id
-- the id of this table has to be unique
-- but it has a default value of 1

CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
