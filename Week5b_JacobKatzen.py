
my_string = ("Arnaa")
print(my_string[1] == "a" and 3 < 5)

musician = "Paul McCartney"
favorite_musician = ("John Lennon")

if musician == favorite_musician:
    print(f"{musician} is the greatest artist of all time")
else:
    print(f"{musician} is not the greatest artist of all time")

# the purpose of this code is to return the absolute value of an integer
num = 7
if num > 0:
    print(num)
else:
    print(num * -1)

professor = "Mr. Smith"
cs_professor = False
if cs_professor == True:
    print(f"{professor} is a cs professor")
else:
    print(f"{professor} is not a cs professor")


gpa = 4.0
if gpa == 4.0:
    print("You are eligible for the award")

countries = ["Brazil", "China", "Cabo Verde", "Haiti", "Portugal", "USA"]
Country = "Italy"

if Country in countries:
    print(f"A student in class was born in {Country}")
else:
    print(f"No student in class was born in {Country}")

# I predict the code will print "pay $12"
# the code does perform as intended the purpose of the code is to print a ticket price based on age
age = 21
if age<=12:
    print("Pay $5.")
if age > 12 and age < 55:
    print("Pay $12.")
if age >= 55:
    print("Pay $8.")

hours = 20
if hours < 0:
    print("error")
elif hours <= 40:
    print(f"You earned ${hours*15}.")
else:
    overtime = (hours - 40) * 22.5
    regular_pay = 40 * 15
    print(f"You earned ${regular_pay + overtime}")

for i in range(1,11):
    print(i)

word = "wow"
if word == word[ : :-1]:
    print("palindrome")
else:
    print("Not palindrome")

n = 8
product = 1
for i in range(1, 9):
    product = product * n
    n = n - 1
print(product)

# this is missing a parentheses after the print statement
# When corrected it should print each fruit in the list
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(fruits[i])


#the code was missing a colon after the if statement
# the code should print all numbers in the list greater than 5
numbers = [2, 6, 3, 8, 10]
for num in numbers:
    if num > 5:
        print(num)


# Question 14: final code will print John can enter
#                                     Sarah can enter
#                                     Mike can not enter
#                                     David cannot enter

# Question 15: final code will print
#fail
# B
# B
# C
# A
# the if block will execute once, the first elif block will execute twice, the second will execute once
# the else will execute once
# the total is 5 times
# each mark gets its grade based on if it falls in the range that the if statements provide