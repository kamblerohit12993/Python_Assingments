#  Employee Payroll Summary

employees = int(input("Enter number of employees: "))

if employees <= 0:
    print("Invalid number of employees!")

else:
    total_net_payroll = 0

    for i in range(1, employees + 1):
        print("\nEmployee", i)

        name = input("Enter employee name: ")
        basic_salary = float(input("Enter basic salary: Rs. "))
        overtime_hours = float(input("Enter overtime hours: "))

        if basic_salary < 0 or overtime_hours < 0:
            print("Invalid salary or overtime hours!")
            continue

        overtime_pay = overtime_hours * 200

        gross_salary = basic_salary + overtime_pay

        if gross_salary >= 50000:
            deduction = gross_salary * 0.10
        else:
            deduction = gross_salary * 0.05

        net_salary = gross_salary - deduction

        total_net_payroll = total_net_payroll + net_salary

        print("\nEmployee Name:", name)
        print("Basic Salary: Rs.", basic_salary)
        print("Overtime Pay: Rs.", overtime_pay)
        print("Gross Salary: Rs.", gross_salary)
        print("Deduction: Rs.", deduction)
        print("Net Salary: Rs.", net_salary)

    print("\n----- Payroll Summary -----")
    print("Total Net Payroll: Rs.", round(total_net_payroll, 2))