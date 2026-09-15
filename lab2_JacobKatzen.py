student_name = "Jacob Katzen "
student_name.rstrip()
student_name.title()

student_major = "cybersecurity"
student_home_town = "Stoughton"
student_age = 18
student_gpa = 4.0

fall_credits, spring_credits = 20,15
total_credits = fall_credits + spring_credits

dream_college = "Harvard"

TUITION_PER_CREDIT = 350
SCHOLARSHIP = 1000
DREAM_TUITION =  5000

fall_cost = fall_credits * TUITION_PER_CREDIT
after_scholarship = fall_cost - SCHOLARSHIP
# I used a plus sign to concatante the variable with the rest of the scentence
#I used .removieprefix to remove "College: " from my print statement
dream_college = "college: Harvard"
print("my dream school is " + str(dream_college.removeprefix("college: ")))

print("-----Dream college profile-----")
print(f"name: {student_name.title()}")
print(f"major: {student_major}")
print(f"home town: {student_home_town}")
print(f"age: {student_age}")
print(f"gpa: {student_gpa}")
print(f"total credits: {total_credits}")
print(f"dream_college: {dream_college.removeprefix('college: ')}")
print(f"dream tuition: {DREAM_TUITION}")
print(f" estimated semester cost: {fall_cost}")
print(f"scholarship: {SCHOLARSHIP}")
print(f"cost after scholarship: {after_scholarship}")
print