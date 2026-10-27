# Program 23: Write a program to calculate the electricity bill based on units consumed.

units = float(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Total electricity bill is: Rs.", bill)

