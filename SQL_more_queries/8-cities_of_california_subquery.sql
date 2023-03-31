-- looking for cities with state='California'
SELECT cities.id, cities.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id
WHERE states.name = 'California'
ORDER BY cities.id ASC;
