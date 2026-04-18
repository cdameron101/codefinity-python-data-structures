animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
animal_movies = list(animal_movies)
animal_movies.append("Dumbo")
animal_movies.append("Zootopia")
animal_movies = tuple(animal_movies)

print("Updated animal movies:", animal_movies)