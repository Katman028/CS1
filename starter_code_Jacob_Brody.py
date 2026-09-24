#Question 1 Jacob Katzen, Brody Sollitto
my_list = list(range(1,20,2))
for value in my_list:
    print(value)

#Question 2
my_list = list(range(3,30,3))
for value in my_list:
    print(value)

#Question 3
my_list = []
for i in range(1,11):
    my_list.append(i**3)
for value in my_list:
 print(value)


#Question 4
my_list = [x**2 for x in range(1,11)]


#Question 5
scores = [78,92,85,64,91,73,88]
scores_copy = scores.copy()

highest_score1 = max(scores)
scores_copy.remove(highest_score1)
highest_score2 = max(scores_copy)

highest_scores = [highest_score1, highest_score2]
print(highest_scores)
#Question 6
numbers = [5,10,15,20,25]
new_list = []

for value in range(len(numbers)):
    new_list.append(numbers[value] * value)
print(new_list)

#Question 7
number = [7,1,5,3,6,4]
new_list = []
for value in range(-1,-7,-1):
    new_list.append(number[value])
print(new_list)


#Question 8
numbers = [10,20,30,40,50,60]
new_list = []
first_slice = numbers[0:3:1]
second_slice = numbers[3:7:1]
second_slice.sort(reverse=True)

for i in range(len(first_slice)):
    new_list.append(first_slice[i])
    new_list.append(second_slice[i])
print(new_list)





#Question 9
numbers = [10,20,30,40,50,60,70,80]
even_numbers = []
odd_numbers = []
for i in range(1,8,2):
    even_numbers.append(numbers[i])
for i in range(0,8,2):
    odd_numbers.append(numbers[i])
print(even_numbers)
print(odd_numbers)


#Question 10
names = ["Alice", "bob", "Charlie", "David"]
scores = [85,92,78,90]
new_list = []
for i in range(0,4):
print(names)

#Question 11
