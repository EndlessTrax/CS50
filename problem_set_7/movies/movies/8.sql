SELECT name from
people JOIN stars ON people.id = stars.person_id
join movies ON stars.movie_id = movies.id
WHERE movies.title = "Toy Story";