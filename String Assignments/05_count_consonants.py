# Program 5: Count the number of consonants in a string

string = input("Enter a string: ")

count = 0

for char in string:
    if char.isalpha() and char.lower() not in "aeiou":
        count += 1

print("Total number of consonants:", count)



