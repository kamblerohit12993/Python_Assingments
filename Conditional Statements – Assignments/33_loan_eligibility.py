# Program 33: Write a program to check whether a person can apply for a loan.

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

if age >= 21:
    if salary >= 30000:
        print("You are eligible to apply for a loan.")
    else:
        print("You are not eligible to apply for a loan due to low salary.")

else:
    print("You are not eligible to apply for a loan due to age.")
    