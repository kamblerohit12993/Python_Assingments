# Program 36: Remove all odd numbers from a list

numbers = [10, 15, 20, 25, 30, 35, 40, 45]

result = []

for num in numbers:
    if num % 2 == 0:
        result.append(num)

print("Original List:", numbers)
print("List after removing odd numbers:", result)



