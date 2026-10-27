# Program 31: Remove punctuation marks from a string

import string

text = input("Enter a string: ")

result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print("String without punctuation:", result)
