#question 1
def countdown(n):
    for i in range(n,0,-1):
        print(i)
    print("blastoff")
countdown(5)

def countdown2(n):
    while n>=0:
        print(n)
        n-=1
    print("blastoff")
countdown2(5)

def countdown3(n):
    if n==0:
        print(n)
        print("blastoff")
    else:
        print(n)
        countdown3(n-1)
countdown3(5)

#question 2
def reverse_word(word):
    if len(word)==1:
        return word
    else:
        return reverse_word(word[1:]) + word[0]
print(reverse_word("abcd"))

#question 3
def maze2():
    #this is where the variable is intiliazed
    response = input("You are lost in a maze. Will you go left or right? ")
    #this is the stop condition
    if response != "left":
        print("You fall in a pit. You lose.")
    else:
        #this is where teh function calls itself
        maze2()
#maze2()

#question 4: True
#question 5: True

#question 6
def count_characters(word):
    if word == "":
        return 0
    else:
        return 1 + count_characters(word[1:])
print(count_characters("hello"))

#question 7
def countdown_2(n):
    if n==0:
        print(n)
    else:
        print(n)
        countdown_2(n-2)
print(countdown_2(10))

#question 8
def contains_letter(word,letter):
    if word == "":
        return False
    else:
        if word[0]==letter:
            return True
        else:
            return contains_letter(word[1:],letter)

print(contains_letter("hello","l"))

#question 9
def repeat_number(n,count=5):
    if count == 0:
        return
    else:
        print(n)
        repeat_number(n,count-1)
repeat_number(5)
