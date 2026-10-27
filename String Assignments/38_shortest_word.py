# Program 38: Find the shortest word in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
shortest = min(words, key=len)

print("Shortest word:", shortest)
print("Length of the word:", len(shortest))
