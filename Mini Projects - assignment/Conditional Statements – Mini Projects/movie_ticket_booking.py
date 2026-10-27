#  Movie Ticket Booking

customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_type = input("Enter show type (Morning/Evening): ").lower()
day_type = input("Enter day type (Weekday/Weekend): ").lower()

if age < 0:
    print("Invalid age!")

elif show_type not in ["morning", "evening"]:
    print("Invalid show type!")

elif day_type not in ["weekday", "weekend"]:
    print("Invalid day type!")

else:
    ticket_price = 200
    discount = 0
    weekend_surcharge = 0

    if age < 12:
        discount = ticket_price * 0.50

    elif age >= 60:
        discount = ticket_price * 0.30

    if show_type == "morning":
        discount = discount + 30

    if day_type == "weekend":
        weekend_surcharge = 50

    final_price = ticket_price - discount + weekend_surcharge

    if final_price < 0:
        final_price = 0

    print("\n----- Movie Ticket Details -----")
    print("Customer Name:", customer_name)
    print("Age:", age)
    print("Original Ticket Price: Rs.", ticket_price)
    print("Total Discount: Rs.", discount)
    print("Weekend Surcharge: Rs.", weekend_surcharge)
    print("Final Ticket Price: Rs.", final_price)
