# Program 28: Check whether a number is Armstrong

num = int(input("Enter a number: "))
original = num
total = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if original == total:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")




