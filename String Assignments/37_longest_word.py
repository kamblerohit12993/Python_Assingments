# Program 37: Find the longest word in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
longest = max(words, key=len)

print("Longest word:", longest)
print("Length of the word:", len(longest))
