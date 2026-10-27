# Program 21: Write a program to find the smallest of three numbers.

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: ")) 

if a <= b and a <= c: 
    print("First number is smallest") 
elif b <= a and b <= c: 
    print("Second number is smallest") 
else: 
    print("Third number is smallest") 

    