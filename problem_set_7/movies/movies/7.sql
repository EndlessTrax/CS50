SELECT title, rating from movies 
JOIN ratings ON ratings.movie_id = movies.id 
WHERE movies.year = 2010 
ORDER BY rating DESC, title;