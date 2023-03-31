-- looking for cities with state='California'
SELECT cities.id, states.name
FROM hbtn_0d_usa.states AS states
INNER JOIN hbtn_0d_usa.cities AS cities
WHERE name = 'California'
ORDER BY cities.id ASC;
