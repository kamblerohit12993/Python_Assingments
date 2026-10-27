# Program 16: Write a program to find the greatest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("first greatest number is:", a)
elif b >= a and b >= c:
    print("second greatest number is:", b)
else:
    print("third greatest number is:", c)
