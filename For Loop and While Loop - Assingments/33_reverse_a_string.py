# Program 33: Print reverse of a string

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string is:", reverse)



