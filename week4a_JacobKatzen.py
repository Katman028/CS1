movies = ["titanic","whiplash","the godfather", "star wars", " star trek"]
movies.append("cars")
movies.append("indiana jones")
movies[0] = "The Matrix"

print(movies[0])
print(movies[-1])
print(len(movies))

for movie in movies:
    print(movie)

slice_movies = movies[:3]
print(slice_movies)

print("question 2")

favorite_pizza = ["pepperoni pizza", "mushroom pizza", "eggplant pizza"]
for pizza in favorite_pizza:
    print(pizza)
for pizza in favorite_pizza:
    print(f"I like {pizza}")
print(f"I really like pizza. \nI like {favorite_pizza[0]}, \n{favorite_pizza[1]} and  \n{favorite_pizza[2]}")
print(f"I really love pizza!")

print("\nquestion 3")
foods = ("cheese burger", "hot dog", "pizza", "chicken nuggets", "mac and cheese")
for food in foods:
    print(food)

print("\n")

foods = ("pasta", "BLT", "pizza", "chicken nuggets", "mac and cheese")
for food in foods:
    print(food)