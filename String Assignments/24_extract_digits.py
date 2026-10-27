# Program 24: Extract only digits from a string

string = input("Enter a string: ")

result = ""

for char in string:
    if char.isdigit():
        result += char

print("Digits in the string:", result)


