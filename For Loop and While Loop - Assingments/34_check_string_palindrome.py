# Program 34: Check whether a string is palindrome

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")





