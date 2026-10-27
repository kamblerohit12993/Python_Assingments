# Program 15: Write a program to check whether a number is divisible by both 3 and 7 or not.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("The number is divisible by both 3 and 7.")
else:
    print("The number is not divisible by both 3 and 7.")
    