# Program 29: Write a program to check blood donation eligibility based on age and weight. 

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 18 and weight >= 50:
    print("You are eligible to donate blood.")
else:
    print("You are not eligible to donate blood.")

    