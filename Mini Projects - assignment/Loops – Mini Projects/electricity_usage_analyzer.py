# Electricity Usage Analyzer

days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days!")

else:
    total_units = 0
    highest_usage = 0
    high_usage_days = 0

    for i in range(1, days + 1):
        units = float(input(f"Enter electricity units for day {i}: "))

        if units < 0:
            print("Invalid units! Please enter again.")
            units = float(input(f"Enter electricity units for day {i}: "))

        total_units = total_units + units

        if units > highest_usage:
            highest_usage = units

        if units > 10:
            high_usage_days = high_usage_days + 1

    average_units = total_units / days

    print("\n----- Electricity Usage Report -----")
    print("Total Units:", total_units)
    print("Average Daily Units:", round(average_units, 2))
    print("Days with Usage Above 10 Units:", high_usage_days)
    print("Maximum Daily Usage:", highest_usage, "units")

    if total_units > 300:
        print("Usage Status: High Usage")
    else:
        print("Usage Status: Normal Usage")