# Program 25: Extract only alphabets from a string

string = input("Enter a string: ")

result = ""

for char in string:
    if char.isalpha():
        result += char

print("Alphabets in the string:", result)
