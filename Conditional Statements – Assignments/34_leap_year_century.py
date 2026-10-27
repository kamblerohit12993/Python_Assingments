# Program 34: Write a program to check whether a year is a leap year and century year.

year = int(input("Enter a year: "))

if year % 100 == 0:
    print("it is a century year.")
    if year % 400 == 0:
        print("it is a leap year.")
    else:
        print("it is not a leap year.")
else:
    print("it is not a century year.")
    if year % 4 == 0:
        print("it is a leap year.")
    else:
        print("it is not a leap year.")



        