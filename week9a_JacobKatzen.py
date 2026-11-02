# # question 1
# from matplotlib import pyplot as plt
#
# rental_car = input("what kind of rental car would you like: ")
# print(f"Let me see if I can find you a {rental_car}")
#
# #question 2
# restaurant_seating = int(input("how many people will be seated: "))
# if restaurant_seating >= 8:
#     print("you will have to wait for a table")
# else:
#     print("your table is ready")
#
# #question 3
# num = int(input("enter a number:"))
# if num % 10 == 0:
#     print("number is a multiple of 10")
# else:
#     print("number is not a multiple of 10")
#
# #question 4
# topping = input("Enter a pizza topping(enter 'quit' to stop): ")
# while topping != "quit":
#     print(f"adding {topping} to the pizza")
#     topping = input("Enter a pizza topping(enter 'quit' to stop): ")
#
# #question 5
# condition = True
# while condition == True:
#     topping = input("Enter a pizza topping(enter 'quit' to stop): ")
#     if topping == "quit":
#         condition = False
#     else:
#         print(f"adding {topping} to the pizza")
#
# condition = True
# while condition == True:
#     topping = input("Enter a pizza topping(enter 'quit' to stop): ")
#     if topping == "quit":
#         break
#     else:
#         print(f"adding {topping} to the pizza")
#
# #question 6
# #condition = True
# #while condition == True:
# #  num = input("enter a number:")
# #  print(num)
#
# #question 7
# sandwich_orders = ["ham and cheese", "grilled cheese", "italian", "steak and cheese"]
# finished_sandwich = []
#
# for sandwich in sandwich_orders:
#     print(f"I made your {sandwich} sandwich")
#     finished_sandwich.append(sandwich)
#
# #question 8
# vacation = input("enter your dream vacation")
# print(f"your dream vacation is {vacation}")

#question 9
import matplotlib.pyplot as plt
# expenses = {}
# food = float(input("How much do you spend on food:"))
# transportation = float(input("How much do you spend on transportation:"))
# entertainment = float(input("How much do you spend on entertainment:"))
# expenses['food'] = food
# expenses['transportation'] = transportation
# expenses['entertainment'] = entertainment
# plt.pie(expenses.values(), labels = expenses.keys())
# plt.show()
# #question 10

# #question 10
# study_times = {}
# math = int(input("how long did you study for math"))
# science = int(input("how long do study for science"))
# english = int(input("how long did you study for english"))
# study_times[math] = math
# study_times[science] = science
# study_times[english] = english
# plt.bar(study_times.keys(), study_times.values())
# plt.title("study times")
# plt.xlabel("math     science    english")
# plt.ylabel("study time(hours)")
# plt.show()

# #question 11
# temperatures = []
# condition = True
# while condition == True:
#     temp = int(input("enter a temperature"))
#     temperatures.append(temp)
#     con = input("do you want to continue (y/n)")
#     if con == "n":
#         condition = False
#     else:
#         condition = True
# print("the temperatures were", temperatures)
# print(f"highest temperature is {max(temperatures)}")
# print(f"lowest temperature is {min(temperatures)}")

#question 12
# grades = {}
# condition = True
# while condition == True:
#     name = input("Enter your name(enter quit to stop): ")
#     if name == "quit":
#         condition = False
#     else:
#         grade = int(input("Enter your grade: "))
#         grades[name] = grade
#
# print(grades)
# average = 0
# for key in grades.keys():
#     average += grades[key]
# average /= len(grades.keys())
# print(f"average grade is {average}")

#question 13
foods = []
