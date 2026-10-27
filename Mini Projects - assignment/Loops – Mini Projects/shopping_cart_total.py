# Shopping Cart Total

products = int(input("Enter number of products: "))

if products <= 0:
    print("Invalid number of products!")

else:
    subtotal = 0

    for i in range(1, products + 1):
        print("\nProduct", i)

        price = float(input("Enter product price: Rs. "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("Invalid price or quantity!")
            continue

        item_total = price * quantity
        subtotal = subtotal + item_total

        print("Item Total: Rs.", item_total)

    print("\n----- Shopping Bill -----")
    print("Subtotal: Rs.", subtotal)

    if subtotal >= 3000:
        discount = subtotal * 0.10
    else:
        discount = 0

    discounted_amount = subtotal - discount

    if discounted_amount < 1500:
        delivery_charge = 100
    else:
        delivery_charge = 0

    grand_total = discounted_amount + delivery_charge

    print("Discount: Rs.", discount)
    print("Amount After Discount: Rs.", discounted_amount)
    print("Delivery Charge: Rs.", delivery_charge)
    print("Grand Total: Rs.", grand_total)