# Program 49: Display menu-driven program using while loop

while True:
    print("\n----- MENU -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting program...")
        break

    if choice >= 1 and choice <= 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Addition:", num1 + num2)

        elif choice == 2:
            print("Subtraction:", num1 - num2)

        elif choice == 3:
            print("Multiplication:", num1 * num2)

        elif choice == 4:
            if num2 != 0:
                print("Division:", num1 / num2)
            else:
                print("Cannot divide by zero")

    else:
        print("Invalid choice. Please try again.")



