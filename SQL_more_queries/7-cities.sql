CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(255),
	state_id INT,
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
