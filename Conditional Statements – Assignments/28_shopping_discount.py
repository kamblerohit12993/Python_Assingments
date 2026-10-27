# Program 28: Write a program to calculate discounts based on total shopping amount.

total_amount = float(input("Enter the total shopping amount: "))

if total_amount >= 5000:
    discount = total_amount * 0.20
elif total_amount >= 3000:
    discount = total_amount * 0.10
elif total_amount >= 1000:
    discount = total_amount * 0.05
else:
    discount = 0

final_amount = total_amount - discount

print("Total shopping amount: Rs.", total_amount)
print("Discount amount: Rs.", discount)



