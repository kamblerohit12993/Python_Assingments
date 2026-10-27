#Program 6: Write a program to compare two numbers and print the greater one.

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")