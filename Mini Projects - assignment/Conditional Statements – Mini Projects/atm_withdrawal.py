# ATM Withdrawal System

account_holder = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

if balance < 0:
    print("Invalid account balance!")

elif withdrawal_amount <= 0:
    print("Invalid withdrawal amount!")

elif withdrawal_amount > 20000:
    print("Transaction Failed: Maximum withdrawal limit is Rs. 20000.")

elif withdrawal_amount > balance:
    print("Transaction Failed: Insufficient balance.")

else:
    remaining_balance = balance - withdrawal_amount

    print("\n----- ATM Transaction Details -----")
    print("Account Holder:", account_holder)
    print("Transaction Status: Successful")
    print("Withdrawn Amount: Rs.", withdrawal_amount)
    print("Remaining Balance: Rs.", remaining_balance)

    if remaining_balance < 1000:
        print("Warning: Low Balance Warning")


