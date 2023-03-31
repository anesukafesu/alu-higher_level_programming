-- displaying all shows and their genre ids
-- those without a genre id are displayed with a null
-- a left join will be appropriate given tv_shows is the left table

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id;
