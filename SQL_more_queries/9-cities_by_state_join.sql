-- display all cities in the format
-- cities.id | cities.name | states.name

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.name
ORDER BY cities.id ASC
