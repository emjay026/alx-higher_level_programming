-- a script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
SELECT a.name AS genre, COUNT(b.show_id) AS number_of_shows
FROM tv_genres a
LEFT JOIN tv_show_genres b ON a.id = b.genre_id
GROUP BY a.name
ORDER BY number_of_shows DESC
