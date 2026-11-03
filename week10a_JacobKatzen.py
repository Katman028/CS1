def calculate_average(a,b,c):
    return (a+b+c)/3

def find_highest(a,b,c):
    #if a>b and a>c:
        #return a
    #elif b>a and b>c:
        #return b
    #elif c>a and c>b:
        #return c
    return max(a,b,c)

def find_lowest(a,b,c):
    #if a<b and a<c:
        #return a
    #elif b<a and b<c:
        #return b
    #elif c<a and c<b:
        #return c
    return min(a,b,c)

def check_pass(score):
    if score>60:
        return True
    else:
        return False

def display_result(name, average):
    print(f"name: {name} average: {average}")

print("===== Student Grade Management =====")
print("1. calculate average")
print("2. find highest")
print("3. find lowest")
print("4. check pass or fail")
print("5. display result")
print("6. exit")
user_choice = int(input("Enter your choice: "))

while user_choice != 6:

    if user_choice == 1:
        score1 = int(input("Enter test score 1: "))
        score2 = int(input("Enter test score 2: "))
        score3 = int(input("Enter test score 3: "))
        print(calculate_average(score1,score2,score3))
        user_choice = int(input("Enter your choice: "))
    elif user_choice == 2:
        score1 = int(input("Enter test score 1: "))
        score2 = int(input("Enter test score 2: "))
        score3 = int(input("Enter test score 3: "))
        print(find_highest(score1,score2,score3))
        user_choice = int(input("Enter your choice: "))
    elif user_choice == 3:
        score1 = int(input("Enter test score 1: "))
        score2 = int(input("Enter test score 2: "))
        score3 = int(input("Enter test score 3: "))
        print(find_lowest(score1,score2,score3))
        user_choice = int(input("Enter your choice: "))
    elif user_choice == 4:
        score1 = int(input("Enter test score 1: "))
        score2 = int(input("Enter test score 2: "))
        score3 = int(input("Enter test score 3: "))
        score = calculate_average(score1,score2,score3)
        print(check_pass(score))
        user_choice = int(input("Enter your choice: "))

    elif user_choice == 5:
        score1 = int(input("Enter test score 1: "))
        score2 = int(input("Enter test score 2: "))
        score3 = int(input("Enter test score 3: "))
        name= input("Enter your name: ")
        average = calculate_average(score1,score2,score3)
        print(display_result(name,average))
        user_choice = int(input("Enter your choice: "))
    elif user_choice == 6:
        break
    else:
        print("invalid choice")
        break






