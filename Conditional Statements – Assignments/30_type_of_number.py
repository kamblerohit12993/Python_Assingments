# Program 30: Write a program to check the type of number (single, double, or three digit).

number = int(input("Enter a number: "))

if -9 <= number <= 9:
    print("Single digit number")
elif -99 <= number <= 99:
    print("Double digit number")
elif -999 <= number <= 999:
    print("Three digit number")
else:
    print("Number has more than three digits")



    