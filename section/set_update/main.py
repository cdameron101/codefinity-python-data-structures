marvel_movies = {
    'Avengers: Endgame',
    'Black Panther',
    'Iron Man'
}

movies_to_add = ('Spider-Man: No Way Home', 'Guardians of the Galaxy')

# Write your code here
movies_to_add = marvel_movies.update(movies_to_add)
movies_to_add = tuple(marvel_movies)

# Testing
print("Updated set:", marvel_movies)