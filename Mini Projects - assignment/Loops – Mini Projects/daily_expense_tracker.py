# Daily Expense Tracker

days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days!")

else:
    total_expense = 0
    highest_expense = 0

    for i in range(1, days + 1):
        expense = float(input(f"Enter expense for day {i}: "))

        if expense < 0:
            print("Invalid expense amount!")
            expense = 0

        total_expense = total_expense + expense

        if expense > highest_expense:
            highest_expense = expense

    average_expense = total_expense / days

    print("\n----- Daily Expense Report -----")
    print("Total Expense: Rs.", total_expense)
    print("Average Daily Expense: Rs.", average_expense)
    print("Highest Daily Expense: Rs.", highest_expense)

    if total_expense > 5000:
        print("Budget Status: Budget Alert")
    else:
        print("Budget Status: Within Budget")