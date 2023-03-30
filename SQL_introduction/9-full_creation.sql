-- create table then add a few rows
CREATE TABLE second_table(id INT, name VARCHAR(256), score INT) IF NOT EXISTS;
INSERT INTO second_table(id, name, score)
SELECT 1, 'John', 10
UNION ALL
SELECT 2, 'Alex', 3
UNION ALL
SELECT 3, 'Bob', 14
UNION ALL
SELECT 4, 'George', 8;
