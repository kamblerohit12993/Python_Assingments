# Program 14: Write a program to check whether a given character is uppercase or lowercase.

ch = input("Enter a character: ")

if ch.isupper() and len(ch) == 1: 
    print("Uppercase character") 
elif ch.islower() and len(ch) == 1: 
    print("Lowercase character") 
else: 
    print("Invalid character")