-- creating cities table with state_id as a foreign key column
-- references id of state table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT,
	name VARCHAR(255),
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
