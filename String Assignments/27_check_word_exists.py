# Program 27: Check whether a word exists in a sentence

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence.split():
    print("Word exists in the sentence.")
else:
    print("Word does not exist in the sentence.")



