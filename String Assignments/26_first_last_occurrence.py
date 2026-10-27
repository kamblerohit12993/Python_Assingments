# Program 26: Find the first and last occurrence of a character

string = input("Enter a string: ")
char = input("Enter a character: ")

first = string.find(char)
last = string.rfind(char)

if first != -1:
    print("First occurrence index:", first)
    print("Last occurrence index:", last)
else:
    print("Character not found in the string.")



