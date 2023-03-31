-- list all shows not linked to the genre of show Dexter

WITH
	dexter_genres AS (
		SELECT tv_show_genres.genre_id AS genre_id
		FROM tv_shows
		INNER JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
		WHERE tv_shows.title = 'Dexter'
	)

SELECT tv_genres.name
FROM dexter_genres
RIGHT JOIN tv_genres
ON dexter_genres.genre_id = tv_genres.id
WHERE dexter_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC
