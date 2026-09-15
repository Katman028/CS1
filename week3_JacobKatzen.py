movie_name ="Star Wars"
genre = "Science Fiction"
release_year = "1985"
rating = 5
#constant for the highest possible rating
HIGHEST_RATING = 5
#multiple assignment for variables
favorite_actor,favorite_character = ("Harrison Ford", "Han Solo")
print("question1")
print("my movie")
print("--------")
print(f" movie: {movie_name}")
print(f" genre: {genre}")
print(f" release year: {release_year}")
print(f" rating: {rating}")
print(f" favorite actor: {favorite_actor}")
print(f" favorite character: {favorite_character}")



people_in_class =  25
groups_of_3 = people_in_class//3
amount_left_over = people_in_class%3
print("question2")
print(f" there is {people_in_class} people class, there can be {groups_of_3} groups of 3, with {amount_left_over} people left")


farenheit = 75
farenheit_to_celsius = (farenheit-32)*5/9
print("question3")
print(f" the weather is {farenheit} degrees farenheit and {farenheit_to_celsius} degrees celsius")
