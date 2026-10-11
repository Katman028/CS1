# question 1
favorite_numbers = {"Jacob": 20, "Gavin": 70, "Mason": 17, "Maddie": 9, "Julia": 7}

for key,value in favorite_numbers.items():
    print(key,value)

#question 2
rivers = {"Nile": "Egypt", "Amazon": "Brazil","Yangtze": "Singapore" }
for key in rivers.keys():
    print(f"The {key} river is in {rivers[key]}")

#question 3
Maggie = {"type of animal": "dog", "owners name":"Mason"}
Charlie = {"type of animal": "cat", "owners name":"Amanda"}
Max = {"type of animal": "hamster", "owners name":"Kyle"}
pets = [Maggie, Charlie, Max]
for pet in pets:
    for key,value in pet.items():
        print(key,value)

print(f"type of animal {pets[0]["type of animal"]}")
print(f"owners name {pets[0]["owners name"]}")

#question 4
favorite_places = {"Jacob": ["gym", "golf course"],
                   "Mason":["basketball court", "baseball field"],
                   "Gavin": ["Hockey rink", "School"]}
for key in favorite_places.keys():
    print(f"{key} favorite places: {favorite_places[key]}")

#question 5
movie_ratings = {"spider man": 9, "star wars": 10, "jaws": 5, "It": 7, "Avengers":8}
for key,value in movie_ratings.items():
    if value > 8:
        print(f"{key,value}")

#question 6
menu = {"Cheese burger": 16, "wings": 14,"steak": 18, "Salad": 12, "soup": 8}
for key,value in menu.items():
    print(f"{key}: {value}")
menu["pizza"] = 11
menu["Cheese burger"] = 17
print("updated menu")
for key,value in menu.items():
    print(f"{key}: {value}")

#question 7
cities = {"Boston": {"population": "600,000", "country": "United States"} ,
          "New York":{ "population": "8.5 million", "country": "United States"} ,
          "Chicago": {"population":"3 million" , "country": "United States"}  }
for key in cities.keys():
    print(f"city name: {key}")
    print(f"city population: {cities[key]['population']}")
    print(f"city country: {cities[key]['country']}")

#question 8
words = ["apple", "banana", "apple", "orange", "banana", "apple", "grapes", "orange"]
num_of_words = {"apple": 3, "banana": 2, "orange": 2, "grapes": 1}

#question 9
courses = {"Math": 15, "English": 25, "Comp Sci": 22, "Biology": 15}
total_students = courses["Math"] + courses["English"] + courses["Biology"]
largest_enrollment = 0
for key, value in courses.items():
    if value > largest_enrollment:
        largest_enrollment = value
    
print(f"largest enrollment:{key} {largest_enrollment}")


#question 10

games = {"fortnite": {"genre":"Action" , "year":"2017", "rating":6 },
"Call of duty":{"genre":"Acion", "year":"2003" , "rating":7} ,
"Madden":{"genre":"Sports", "year":"2026", "rating":10}}

games["fifa"] = {"genre": "sports", "year":"2026", "rating":9}
games["rocket league"] = {"genre": "Sports", "year":"2015" , "rating":6}

for key,value in games.items():
    if games[key]["rating"] >= 9:
        print(f"{key}: {value}")

print(f"{games["fortnite"]["genre"]},{games["fortnite"]['rating']}")


