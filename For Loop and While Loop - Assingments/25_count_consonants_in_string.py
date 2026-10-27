# Program 25: Count consonants in a string

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count = count + 1

print("Number of consonants:", count)




