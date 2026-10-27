# Program 43: Calculate sum of cubes of first n numbers

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + (i * i * i)

print("Sum of cubes is:", total)



