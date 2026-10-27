# Program 50: Write a program to build a simple ATM menu using a match case.


balance = 5000

print("Welcome to ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        print("Your balance is:", balance)

    case 2:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully")
            print("Your balance is:", balance)
        else:
            print("Invalid amount")

    case 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance = balance - amount
            print("Please collect your cash")
            print("Your balance is:", balance)
        else:
            print("Insufficient balance")

    case _:
        print("Invalid choice")