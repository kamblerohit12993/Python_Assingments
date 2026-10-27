# Program 4: Count the number of vowels in a string

string = input("Enter a string: ")

count = 0

for char in string:
    if char.lower() in "aeiou":
        count += 1

print("Total number of vowels:", count)



