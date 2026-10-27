import random

zoo = {"exhibit1": ["lion","tiger", "bear"],
       "exhibit2": ["monkey", "gorilla", "zebra"],
       "exhibit3":["eagle","peacock","chicken"],
       "exhibit4:":["elephant", "giraffe", "llama"]}
visitor_counts= []
counter = 0
for key,value in zoo.items():
    visitor_counts.append(random.randint(10,100))
    print(f"exhibit {key}")
    print(f"animals {value}")
    print(f"visitors {visitor_counts[counter]}")
    counter += 1



