#  Text Analyzer System

text = input("Enter a sentence or paragraph: ")

text = " ".join(text.split())

characters = len(text)
words = text.split()
word_count = len(words)
sentence_count = text.count(".") + text.count("!") + text.count("?")

vowels = 0
consonants = 0
digits = 0
special_characters = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special_characters += 1

print("\n--- Text Analysis Report ---")
print("Total Characters:", characters)
print("Total Words:", word_count)
print("Total Sentences:", sentence_count)
print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
print("Total Digits:", digits)
print("Total Special Characters:", special_characters)

print("Uppercase Text:", text.upper())
print("Lowercase Text:", text.lower())

search_word = input("\nEnter a word to search: ")

if search_word.lower() in [word.lower() for word in words]:
    print("Word found in the text.")
else:
    print("Word not found in the text.")

print("\n--- Word Frequency ---")

frequency = {}

for word in words:
    word = word.lower().strip(".,!?;:\"'()[]{}")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(word, ":", count)
