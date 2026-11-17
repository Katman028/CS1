def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n-1)
print(sum_numbers(5))


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
print(fac(5))


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
print(power(2, 3))


print("===== RECURSIVE NUMBER EXPLORER =====\n1. Sum of Natural Numbers\n2. Factorial Calculator\n3. Power Calculator\nQuit")
user_choice = input("enter your choice")
while user_choice != "quit":
    if user_choice == "1":
       n=  int(input("enter non neggative number"))
       print(sum_numbers(n))
       user_choice = input("enter your choice")
       print(
           "===== RECURSIVE NUMBER EXPLORER =====\n1. Sum of Natural Numbers\n2. Factorial Calculator\n3. Power Calculator\nQuit")
    elif user_choice == "2":
        n= int(input("enter non negative number"))
        print(fac(n))
        user_choice = input("enter your choice")
        print(
            "===== RECURSIVE NUMBER EXPLORER =====\n1. Sum of Natural Numbers\n2. Factorial Calculator\n3. Power Calculator\nQuit")
    elif user_choice == "3":
        base= int(input("enter non negative number"))
        exp = int(input("enter exponent"))
        print(power(base,exp))
        print(
            "===== RECURSIVE NUMBER EXPLORER =====\n1. Sum of Natural Numbers\n2. Factorial Calculator\n3. Power Calculator\nQuit")
        user_choice = input("enter your choice")
