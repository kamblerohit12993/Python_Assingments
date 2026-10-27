# Hotel Room Booking System

guest_name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ").lower()
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Invalid number of nights!")

elif room_type not in ["standard", "deluxe", "suite"]:
    print("Invalid room type!")

else:
    if room_type == "standard":
        price_per_night = 2000

    elif room_type == "deluxe":
        price_per_night = 3500

    else:
        price_per_night = 6000

    room_charge = price_per_night * nights

    if nights >= 10:
        discount = room_charge * 0.20

    elif nights >= 5:
        discount = room_charge * 0.10

    else:
        discount = 0

    final_amount = room_charge - discount

    print("\n----- Hotel Booking Details -----")
    print("Guest Name:", guest_name)
    print("Room Type:", room_type.capitalize())
    print("Number of Nights:", nights)
    print("Room Charge: Rs.", room_charge)
    print("Discount: Rs.", discount)
    print("Final Booking Amount: Rs.", final_amount)
