ages = [4,10,16,25,70]

for age in ages:
    if age <= 5:
        print(f" the age is {age} The ticket price is $0")
    elif age <= 12 and age > 5:
        print(f" the age is {age} The ticket price is $8")
    elif age <= 17 and age > 12:
        print(f" the age is {age} The ticket price is $10")
    elif age <= 64 and age > 17:
        print(f" the age is {age} The ticket price is $15")
    else:
        print(f" the age is {age} The ticket price is $10")
