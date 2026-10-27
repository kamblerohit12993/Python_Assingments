# Program 10: Find the index of a given character in a string

string = input("Enter a string: ")
char = input("Enter a character: ")

index = string.find(char)

if index != -1:
    print("Index of the character:", index)
else:
    print("Character not found in the string.")



