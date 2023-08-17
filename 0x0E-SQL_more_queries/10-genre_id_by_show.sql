-- a script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT title, genre_id
FROM tv_shows a, tv_show_genres b
WHERE a.id = b.show_id
ORDER BY a.title ASC, b.genre_id ASC;
