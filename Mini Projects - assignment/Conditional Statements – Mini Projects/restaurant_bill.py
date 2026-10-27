# Restaurant Bill and Service Charge

customer_name = input("Enter customer name: ")
bill_amount = float(input("Enter food bill amount: "))
membership = input("Do you have membership? (Yes/No): ").lower()

if bill_amount < 0:
    print("Invalid bill amount!")

elif membership not in ["yes", "no"]:
    print("Invalid membership status!")

else:
    if bill_amount < 1000:
        discount_percentage = 0

    elif bill_amount < 3000:
        discount_percentage = 5

    elif bill_amount < 5000:
        discount_percentage = 10

    else:
        discount_percentage = 15

    if membership == "yes":
        discount_percentage = discount_percentage + 5

    discount = bill_amount * discount_percentage / 100

    amount_after_discount = bill_amount - discount

    service_charge = amount_after_discount * 5 / 100

    final_amount = amount_after_discount + service_charge

    print("\n----- Restaurant Bill -----")
    print("Customer Name:", customer_name)
    print("Original Bill: Rs.", bill_amount)
    print("Discount Percentage:", discount_percentage, "%")
    print("Discount Amount: Rs.", discount)
    print("Service Charge: Rs.", service_charge)
    print("Final Payable Amount: Rs.", final_amount)

    if final_amount >= 5000:
        print("Thank you for being a valued customer")


