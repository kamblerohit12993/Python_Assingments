# Program 29: Replace a word with another word in a sentence

sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

new_sentence = sentence.replace(old_word, new_word)

print("Updated sentence:", new_sentence)


