# Program 48: Write a program to print language choice using match case.

print("Select your language:")
print("1. English")
print("2. Marathi")
print("3. Hindi")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        print("You selected English")
    case 2:
        print("You selected Marathi")
    case 3:
        print("You selected Hindi")
    case _:
        print("Invalid choice")



        