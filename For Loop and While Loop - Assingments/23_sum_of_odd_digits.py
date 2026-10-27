# Program 23: Find sum of odd digits in a number

num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        total = total + digit

    num = num // 10

print("Sum of odd digits is:", total)





