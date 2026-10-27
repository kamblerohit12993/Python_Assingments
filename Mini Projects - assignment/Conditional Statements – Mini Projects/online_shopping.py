# Online Shopping Checkout

customer_name = input("Enter customer name: ")
purchase_amount = float(input("Enter purchase amount: "))
customer_type = input("Enter customer type (Regular/Premium): ").lower()

if purchase_amount < 0:
    print("Invalid purchase amount!")

elif customer_type != "regular" and customer_type != "premium":
    print("Invalid customer type!")

else:
    if purchase_amount >= 5000:
        discount = purchase_amount * 0.20
    elif purchase_amount >= 3000:
        discount = purchase_amount * 0.10
    elif purchase_amount >= 1000:
        discount = purchase_amount * 0.05
    else:
        discount = 0

    if customer_type == "premium":
        discount = discount + (purchase_amount * 0.05)

    amount_after_discount = purchase_amount - discount

    if amount_after_discount >= 2000:
        delivery_charge = 0
    else:
        delivery_charge = 100

    final_amount = amount_after_discount + delivery_charge

    print("\n----- Online Shopping Bill -----")
    print("Customer Name:", customer_name)
    print("Customer Type:", customer_type.capitalize())
    print("Purchase Amount: Rs.", purchase_amount)
    print("Discount Amount: Rs.", discount)
    print("Delivery Charge: Rs.", delivery_charge)
    print("Final Payable Amount: Rs.", final_amount)
