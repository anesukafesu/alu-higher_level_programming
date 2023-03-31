-- looking for cities with state='California'
SELECT cities.id, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id
WHERE name = 'California'
ORDER BY cities.id ASC;
