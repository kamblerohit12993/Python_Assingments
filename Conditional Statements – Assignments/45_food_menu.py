# Program 45: Write a program to print menu-based food selection using match case.

print("Food Menu")
print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
print("4. Pasta")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Sandwich")
    case 4:
        print("You selected Pasta")
    case _:
        print("Invalid choice")

        