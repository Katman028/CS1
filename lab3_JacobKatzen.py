import random
secret_words = ["home", "computer", "science", "python", "code"]
guessed_letters = []
incorrect_guess = 0
max_guesses = 6
secret_word = random.choice(secret_words)

def display_word():
    for i in range(0,len(secret_word)):
        if secret_word[i] in guessed_letters:
            print(secret_word[i],end=" ")
        else:
            print("_",end=" ")

def check_game_status():
    if incorrect_guess == max_guesses:
        print("you lose")
        print(f"secret word: {secret_word}")
        return False
    elif incorrect_guess < max_guesses:
        for i in range (len(secret_word)):
            if secret_word[i] in guessed_letters and len(guessed_letters) - incorrect_guess >= len(secret_word):
                print("congratulations! you win")
                print(f"secret word: {secret_word}")
                return False

            else:
                return True




def play_game():
    global incorrect_guess
    while check_game_status() == True:
        print("secret word:")
        display_word()
        print(f"\nguessed letters {guessed_letters}")
        print(f"incorrect guesses remaining: {max_guesses - incorrect_guess}")
        user_guess = input("Enter your guess: ")
        user_guess = user_guess.lower()
        if user_guess in guessed_letters:
            user_guess = input("Enter a new guess: ")
        else:
            guessed_letters.append(user_guess)
            if user_guess not in secret_word:
                print("Wrong guess. Try again\n")

                incorrect_guess += 1






play_game()






