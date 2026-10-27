#  Bank Transaction History

balance = float(input("Enter opening balance: Rs. "))
transactions = int(input("Enter number of transactions: "))

if balance < 0 or transactions < 0:
    print("Invalid opening balance or number of transactions!")

else:
    deposits = 0
    successful_withdrawals = 0
    rejected_withdrawals = 0

    for i in range(1, transactions + 1):
        print("\nTransaction", i)
        print("1. Deposit")
        print("2. Withdrawal")

        choice = input("Enter transaction type (1 or 2): ")
        amount = float(input("Enter amount: Rs. "))

        if amount <= 0:
            print("Invalid transaction amount!")

        elif choice == "1":
            balance = balance + amount
            deposits = deposits + 1
            print("Deposit Successful!")

        elif choice == "2":
            if amount <= balance:
                balance = balance - amount
                successful_withdrawals = successful_withdrawals + 1
                print("Withdrawal Successful!")
            else:
                rejected_withdrawals = rejected_withdrawals + 1
                print("Insufficient Balance! Withdrawal Rejected.")

        else:
            print("Invalid transaction type!")

    print("\n----- Bank Transaction Summary -----")
    print("Final Balance: Rs.", round(balance, 2))
    print("Total Deposits:", deposits)
    print("Successful Withdrawals:", successful_withdrawals)
    print("Rejected Withdrawals:", rejected_withdrawals)

    if balance < 1000:
        print("Warning: Your balance is below Rs. 1000!")