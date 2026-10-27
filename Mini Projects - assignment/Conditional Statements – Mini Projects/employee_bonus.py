# Employee Performance Bonus

employee_name = input("Enter employee name: ")
monthly_salary = float(input("Enter monthly salary: "))
experience = float(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

if monthly_salary < 0 or experience < 0:
    print("Invalid salary or experience!")

elif rating < 1 or rating > 5:
    print("Invalid rating! Rating must be between 1 and 5.")

else:
    if experience >= 10 and rating >= 4:
        bonus_percentage = 20

    elif experience >= 5 and rating >= 4:
        bonus_percentage = 15

    elif experience >= 2 and rating >= 3:
        bonus_percentage = 10

    else:
        bonus_percentage = 0

    bonus_amount = monthly_salary * bonus_percentage / 100
    final_salary = monthly_salary + bonus_amount

    print("\n----- Employee Bonus Details -----")
    print("Employee Name:", employee_name)
    print("Monthly Salary: Rs.", monthly_salary)
    print("Bonus Percentage:", bonus_percentage, "%")
    print("Bonus Amount: Rs.", bonus_amount)
    print("Final Salary: Rs.", final_salary)

    if rating == 5:
        print("Performance Message: Excellent Performer")
    else:
        print("Performance Message: Keep Improving")
