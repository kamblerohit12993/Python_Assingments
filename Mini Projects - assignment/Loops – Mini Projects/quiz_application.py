#  Quiz Application

score = 0

print("Welcome to the Quiz Application!")
print("Answer the following 5 questions.\n")

# Question 1
print("1. Which language are we learning?")
print("a) Java")
print("b) Python")
print("c) C++")
answer = input("Enter your answer: ").lower()

if answer == "b":
    score = score + 1

# Question 2
print("\n2. Which function is used to display output in Python?")
print("a) print()")
print("b) input()")
print("c) display()")
answer = input("Enter your answer: ").lower()

if answer == "a":
    score = score + 1

# Question 3
print("\n3. Which loop is used to repeat code in Python?")
print("a) repeat")
print("b) for")
print("c) stop")
answer = input("Enter your answer: ").lower()

if answer == "b":
    score = score + 1

# Question 4
print("\n4. Which symbol is used for multiplication?")
print("a) +")
print("b) -")
print("c) *")
answer = input("Enter your answer: ").lower()

if answer == "c":
    score = score + 1

# Question 5
print("\n5. Which data type stores True or False?")
print("a) int")
print("b) bool")
print("c) str")
answer = input("Enter your answer: ").lower()

if answer == "b":
    score = score + 1

# Calculate percentage
percentage = (score / 5) * 100

print("\n----- Quiz Result -----")
print("Total Questions: 5")
print("Correct Answers:", score)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Performance: Excellent!")
elif percentage >= 60:
    print("Performance: Good!")
else:
    print("Performance: Keep Practicing!")