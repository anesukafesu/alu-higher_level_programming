-- display all non-comedy tv shows

WITH summarise_genres AS (
	SELECT tv_show_genres.show_id, GROUP_CONCAT(tv_genres.name SEPARATOR ', ') AS genres
	
	FROM tv_show_genres
	LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	GROUP BY tv_show_genres.show_id
)

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN summarise_genres
ON tv_shows.id = summarise_genres.show_id
WHERE summarise_genres.genres NOT LIKE '%Comedy%'
ORDER BY tv_shows.title;
