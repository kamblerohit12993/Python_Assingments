# Program 7: Write a program to check whether a character is a vowel or consonant.

ch = input("Enter a character: ") 
if ch.lower() in "aeiou" and len(ch) == 1 and ch.isalpha(): 
    print("Vowel") 
elif len(ch) == 1 and ch.isalpha(): 
    print("Consonant") 
else: 
    print("Please enter a single alphabet")