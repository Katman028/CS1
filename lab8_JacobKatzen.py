import random

def generate_secret_number():
    secret_number = random.randint(1,20)
    print(f"(the secret number is {secret_number})")
    return secret_number

def play_guessing_game():
    secret_number = generate_secret_number()
    user_guess = int(input("guess the secret number"))
    for i in range(0,5):
        if user_guess > secret_number:
            print("too high")
            user_guess = int(input("guess the secret number"))
        elif user_guess < secret_number:
            print("too low")
            user_guess = int(input("guess the secret number"))
        elif user_guess == secret_number:
            print("good job")
            user_guess = int(input("guess the secret number"))
            break



def play_quik_quiz():
    score = 0
    random_number1 = random.randint(1,10)
    random_number2 = random.randint(1,10)
    user_answer = int(input(f" add {random_number1} and {random_number2}"))
    if user_answer == random_number1 + random_number2:
        print("good job you earned 1 point")
        score += 1
    else:
        print("wrong answer")

def main():
    print("===== PYTHON CHALLENGE GAME ===== /n 1. Play the guessing game /n 2. Take a quick math quiz /n 3. Exit")
    user_choice = int(input("enter your choice"))
    while user_choice != 3:
        if user_choice == 1:
            play_guessing_game()
            user_choice = int(input("enter your choice"))
        elif user_choice == 2:
            play_quik_quiz()
            user_choice = int(input("enter your choice"))
        elif user_choice == 3:
            break
        else:
            print("invalid choice")
            break
main()