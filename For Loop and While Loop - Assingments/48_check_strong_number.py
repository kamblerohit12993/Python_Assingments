# Program 48: Check whether a number is a strong number

num = int(input("Enter a number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    temp = temp // 10

if total == num:
    print("It is a Strong Number")
else:
    print("It is not a Strong Number")




